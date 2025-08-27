from get_compass_file import get_file_from_compass, get_last_downloaded_file
from process_compass import unzip_file, run_uff_for_all
from setup import zip_and_archive

"""

downloads, unzips and deciphers the latest file from the NBIN Compass system.
"""

if __name__ == "__main__":
    try:
        zip_and_archive()
    except FileNotFoundError:
        pass

    get_file_from_compass()
    last_file = get_last_downloaded_file()
    unzip_file(last_file)
    run_uff_for_all()
