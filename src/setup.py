from os import path, makedirs, walk
import zipfile
import datetime
import shutil

from constants import DOWNLOADS_FOLDER, ARCHIVE_FOLDER


def zip_and_archive(source_dir=DOWNLOADS_FOLDER, archive_dir=ARCHIVE_FOLDER):
    """
    Zips all files in the source directory and moves the zip file to the archive directory.

    Args:
        source_dir (str): Path to the directory containing files to be zipped.
        archive_dir (str): Path to the directory where the zipped file will be moved.
    """

    source_dir = path.join(source_dir, "processing")

    if not path.exists(source_dir):
        raise FileNotFoundError(f"Processing directory not found: {source_dir}")

    makedirs(archive_dir, exist_ok=True)

    now = datetime.datetime.now()
    archive_name = now.strftime("%Y%m%d_%H%M%S") + ".zip"
    archive_path = path.join(archive_dir, archive_name)

    with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in walk(source_dir):
            for file in files:
                file_path = path.join(root, file)
                zipf.write(file_path, path.relpath(file_path, source_dir))

    print(f"Successfully zipped and archived to: {archive_path}")

    shutil.rmtree(source_dir)
    print(f"Successfully removed source directory: {source_dir}")
