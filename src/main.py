from db import get_mysql_engine_from_env
from get_compass_file import get_file_from_compass, get_last_downloaded_file
from process_compass import unzip_file, run_uff_for_all
from setup import zip_and_archive
from slack_alert import send_alert
from upload_out_to_db import DEFAULT_OUT_DIR, upload_all_csvs

"""

downloads, unzips and deciphers the latest file from the NBIN Compass system.
"""

if __name__ == "__main__":
    try:
        zip_and_archive()
        get_file_from_compass()
        last_file = get_last_downloaded_file()
        unzip_file(last_file)
        run_uff_for_all()

        engine = get_mysql_engine_from_env()
        s, f = upload_all_csvs(out_dir=DEFAULT_OUT_DIR, engine=engine)
        send_alert(f'{s}, {f}')

    except FileNotFoundError:
        send_alert('Files not found.')

    except Exception as e:
        send_alert(f':scream: {e}')

