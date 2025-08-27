import subprocess
import os

def convert_all_uff_to_csv(directory):
    """
    Converts all UFF files in a directory to CSV using the uffconv command.

    Args:
        directory (str): The path to the directory containing UFF files.
    """

    successes = []
    failures = []

    for filename in os.listdir(directory):
        if filename.endswith(".UFF") or filename.endswith(".uff"):  # Case-insensitive check
            uff_file_path = os.path.join(directory, filename)
            print(f"Processing {uff_file_path}...")

            try:
                # Replace with the actual path to uffconv on your system
                uffconv_path = "uffconv"  # Example path - CHANGE THIS!  It needs to be in your PATH or be a full path
                output_dir = "downloads/processing"  # CHANGE THIS!
                odf_file = "/path/to/FileCab.odf"  # CHANGE THIS!
                log_file = "/path/to/run.log" # CHANGE THIS!

                # Construct the command
                command = [
                    uffconv_path,
                    uff_file_path,
                    "/fnul",
                    "/out", output_dir,
                    "/odf", odf_file,
                    "/csv",
                    "/titles",
                    "/summary"
                ]

                # Execute the command
                process = subprocess.Popen(command,
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE)
                stdout, stderr = process.communicate()

                # Print the output and error messages
                print("Output:", stdout.decode())
                if stderr:
                    print("Error:", stderr.decode())

                # Check the return code
                if process.returncode != 0:
                    print(f"Error: uffconv failed with return code {process.returncode}")
                    failures.append(uff_file_path)
                else:
                    successes.append(uff_file_path)

            except FileNotFoundError:
                print("Error: uffconv not found.  Make sure the path is correct.")
                failures.append(uff_file_path)
            except Exception as e:
                print(f"An error occurred: {e}")
                failures.append(uff_file_path)

    if successes:
        print("\nSuccessfully converted the following files:")
        for file in successes:
            print(file)

    if failures:
        print("\nFailed to convert the following files:")
        for file in failures:
            print(file)

    return successes, failures

if __name__ == '__main__':
    # Example Usage (for testing):
    processing_directory = "downloads/processing"  # Replace with your actual directory
    successes, failures = convert_all_uff_to_csv(processing_directory)
