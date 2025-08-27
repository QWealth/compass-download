from os import path, makedirs, listdir
from zipfile import ZipFile, BadZipFile
import shutil

import subprocess
import platform

from constants import DOWNLOADS_FOLDER, PROCESSING_FILENAME

DESTINATION_FOLDER = "C:/uff/in"


def unzip_file(zip_file, base_dir=DOWNLOADS_FOLDER):
    """
    Unzips a zip file into a directory named 'processing' in the same directory
    as the zip file, then moves the extracted files to C:/uff/in.
    """
    zip_file_path = path.join(path.abspath(base_dir), zip_file)
    extract_dir = path.join(path.dirname(zip_file_path), PROCESSING_FILENAME)
    makedirs(extract_dir, exist_ok=True)
    makedirs(DESTINATION_FOLDER, exist_ok=True)

    try:
        with ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
        print(f"Successfully extracted: '{extract_dir}'")
        for item in path.listdir(extract_dir):
            s = path.join(extract_dir, item)
            d = path.join(DESTINATION_FOLDER, item)
            shutil.move(s, d)
        
        print(f"Files moved to: '{DESTINATION_FOLDER}'")
        return DESTINATION_FOLDER
    except BadZipFile:
        print(f"Error: '{zip_file_path}' is not a valid zip file.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def run_uff_for_all(destination_folder=DESTINATION_FOLDER, uff_bat_path="C:/uff/uff.bat"):
    """
    Runs the uff.bat for every file in destination_folder.

    - destination_folder: directory containing input files (e.g. C:/uff/in)
    - uff_bat_path: full path to uff.bat (default C:/uff/uff.bat)

    Returns (successes, failures) lists of filenames.
    Raises FileNotFoundError if uff.bat is missing or destination_folder is missing.
    """
    if not path.exists(destination_folder):
        raise FileNotFoundError(f"Destination folder not found: {destination_folder}")

    if not path.exists(uff_bat_path):
        raise FileNotFoundError(f"uff.bat not found: {uff_bat_path}")

    successes = []
    failures = []

    # Ensure we're on Windows - .bat requires Windows environment
    if platform.system() != "Windows":
        raise RuntimeError("uff.bat execution requires Windows. Run this on Windows or use the native uffconv on macOS.")

    for name in listdir(destination_folder):
        input_path = path.join(destination_folder, name)
        if not path.isfile(input_path):
            continue

        print(f"Running uff.bat for: {input_path}")
        # Use the batch file directly; subprocess will run the .bat on Windows
        try:
            proc = subprocess.run([uff_bat_path, input_path],
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE,
                                  text=True,
                                  check=False)

            if proc.returncode == 0:
                print(f"Success: {name}")
                successes.append(name)
            else:
                print(f"Failed ({proc.returncode}): {name}")
                print(proc.stdout)
                print(proc.stderr)
                failures.append((name, proc.returncode, proc.stderr))
        except Exception as e:
            print(f"Exception while processing {name}: {e}")
            failures.append((name, str(e)))

    return successes, failures

