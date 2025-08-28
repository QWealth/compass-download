import os
from os import path
import pandas as pd

from sqlalchemy import inspect, text

from db import get_mysql_engine_from_env
from table_definitions import table_index

DEFAULT_OUT_DIR = "C:/uff/out"
# DEFAULT_OUT_DIR = '../test_files'


def _derive_key_from_filename(filename):
    base = path.basename(filename)
    name, ext = path.splitext(base)
    return name.lower()


def remake_table(engine, table_name, model):
    """
    Drops table_name if it exists, then recreates it using the SQLAlchemy model's definition.
    Intended to be called *before* inserting data (since dropping wipes contents).
    """
    insp = inspect(engine)

    if insp.has_table(table_name):
        model.__table__.drop(engine, checkfirst=True)
        model.__table__.create(engine, checkfirst=True)


def upload_all_csvs(out_dir=DEFAULT_OUT_DIR, engine=None, if_exists='replace', read_csv_kwargs=None):
    """
    Upload every CSV (or TXT) from out_dir to MySQL using SQLAlchemy engine.
    Table name is derived from the filename.

    Args:
      out_dir (str): directory containing CSV files
      engine: SQLAlchemy engine. If None, created from env vars via get_mysql_engine_from_env()
      if_exists: passed to pandas.DataFrame.to_sql ('replace'|'append'|'fail')
      read_csv_kwargs: optional dict passed to pandas.read_csv

    Returns:
      (successes, failures) lists.
      successes contain tuples (filename, table_name, num_records).
      failures contain tuples (filename, error).
    """
    if engine is None:
        engine = get_mysql_engine_from_env()

    if read_csv_kwargs is None:
        read_csv_kwargs = {}

    if not path.exists(out_dir):
        raise FileNotFoundError(f"Output directory not found: {out_dir}")

    successes = []
    failures = []

    for fname in os.listdir(out_dir):
        fpath = path.join(out_dir, fname)
        if not path.isfile(fpath):
            continue

        lower_fname = fname.lower()
        if not lower_fname.endswith('.txt'):
            print(f'skipping {lower_fname}')
            continue

        key = _derive_key_from_filename(fname)
        model = table_index.get(key)
        table_name: str = model.__tablename__

        # remake_table(engine, table_name, model)

        try:
            df = pd.read_csv(fpath, **read_csv_kwargs)
            num_records = len(df)

            df.to_sql(table_name, con=engine, if_exists='append', index=False)

            successes.append((fname, table_name, num_records))
            print(f"Uploaded {fname} -> {table_name} ({num_records} records)")
        except Exception as exc:
            failures.append((fname, str(exc)))
            print(f"Failed to upload {fname}: {exc}")

    return successes, failures


if __name__ == "__main__":
    engine = None
    try:
        engine = get_mysql_engine_from_env()
    except Exception as e:
        print(f"DB engine creation failed: {e}")
        raise

    out_dir = DEFAULT_OUT_DIR
    s, f = upload_all_csvs(out_dir=out_dir, engine=engine)
    print("Successes:", s)
    print("Failures:", f)
