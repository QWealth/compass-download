import os
from sqlalchemy import create_engine

def get_mysql_engine_from_env(echo=False, pool_pre_ping=True):
    """
    Create and return a SQLAlchemy engine for MySQL using environment variables:
      DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

    Raises:
      EnvironmentError if required env vars are missing.
    """
    passwords = {
        "password": "Wmd5DtejL00Yo7vcOKcQKCf0EyQltGPP",
        "engine": "mysql",
        "port": 3306,
        "dbInstanceIdentifier": "fundfactsbackend-fundfactdatabasefe4a77b3-w1biyycw11sr",
        "host": "fundfactsbackend-fundfactdatabasefe4a77b3-w1biyycw11sr.criwycoituxs.ca-central-1.rds.amazonaws.com"
    }
    user = os.getenv("DB_USER", 'admin')
    password = os.getenv("DB_PASS", passwords["password"])
    host = os.getenv("DB_HOST", passwords["host"])
    port = os.getenv("DB_PORT", "3306")
    db = os.getenv("DB_NAME", "default")

    if not all([user, password, db]):
        raise EnvironmentError(
            "DB_USER, DB_PASS and DB_NAME environment variables must be set"
        )

    # Uses pymysql driver; ensure 'pymysql' is installed in the environment
    url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}?charset=utf8mb4"
    engine = create_engine(url, echo=echo, pool_pre_ping=pool_pre_ping)
    return engine

def get_engine_from_url(url, echo=False, pool_pre_ping=True):
    """Create engine from a full SQLAlchemy URL."""
    return create_engine(url, echo=echo, pool_pre_ping=pool_pre_ping)