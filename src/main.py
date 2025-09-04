from db import get_mysql_engine_from_env, get_qc_engine
from get_compass_file import get_file_from_compass, get_last_downloaded_file
from process_compass import unzip_file, run_uff_for_all
from setup import zip_and_archive
from slack_alert import send_alert
from upload_out_to_db import DEFAULT_OUT_DIR, upload_all_csvs

"""

downloads, unzips and deciphers the latest file from the NBIN Compass system.
"""

from datetime import date, timedelta


def was_yesterday_weekend() -> bool:
    yesterday = date.today() - timedelta(days=1)
    return yesterday.weekday() >= 5


def format_successes(successes):
    if not successes:
        return "No files were uploaded successfully."
    lines = []
    for fname, table, num_records in successes:
        lines.append(f"- {fname} → {table} ({num_records} records)")
    return "\n".join(lines)


if __name__ == "__main__":
    if was_yesterday_weekend():
        send_alert('yesterday was weekend.')
        exit()

    try:
        zip_and_archive()
        get_file_from_compass()
        last_file = get_last_downloaded_file()
        unzip_file(last_file)
        run_uff_for_all()

        engine = get_mysql_engine_from_env()
        qc_engine = get_qc_engine()
        s, f = upload_all_csvs(out_dir=DEFAULT_OUT_DIR, engines=[engine, qc_engine])
        send_alert(format_successes(s))
        if len(f):
            send_alert(str(f))

    except FileNotFoundError:
        send_alert('Files not found.')

    except Exception as e:
        send_alert(f':scream: {e}')

