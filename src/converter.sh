import subprocess
import os

def convert_uff_to_csv(uff_file_path):
    """
    Converts a UFF file to CSV using the uffconv command.

    Args:
        uff_file_path (str): The full path to the UFF file.
    """

    try:
        # Replace with the actual path to uffconv on your system
        uffconv_path = "uffconv"  # Example path - CHANGE THIS!
        output_dir = "output"  # CHANGE THIS!
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
            return False

        return True

    except FileNotFoundError:
        print("Error: uffconv not found.  Make sure the path is correct.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Example usage:
# Assuming you have the path to the UFF file
# uff_file = "path/to/your/data.UFF"
# success = convert_uff_to_csv(uff_file)
# if success:
#     print("UFF file converted successfully!")
# else:
#     print("UFF conversion failed.")
