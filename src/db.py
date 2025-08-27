import os
from sqlalchemy import create_engine

def get_mysql_engine_from_env(echo=False, pool_pre_ping=True):
    """
    Create and return a SQLAlchemy engine for MySQL using environment variables:
      DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

    Raises:
      EnvironmentError if required env vars are missing.
    """
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASS")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "3306")
    db = os.getenv("DB_NAME")

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