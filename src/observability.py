import os
import socket
from typing import Optional

import sentry_sdk


def init_observability(app_name: str = "seleniumFun", dsn: Optional[str] = None) -> None:
    """
    Initialize Sentry if SENTRY_DSN is provided via arg or environment.
    Safe to call multiple times; subsequent calls are ignored by SDK.
    """
    dsn = dsn or os.getenv("SENTRY_DSN", "https://59aeb3cf34f043bc90c629a123fc1a6e@o1168654.ingest.sentry.io/6262116")
    if not dsn:
        return

    environment = (
        os.getenv("APP_ENV")
        or os.getenv("ENV")
        or os.getenv("ENVIRONMENT")
        or "production"
    )

    release = os.getenv("APP_RELEASE") or os.getenv("GIT_COMMIT")

    sentry_sdk.init(
        dsn=dsn,
        environment=environment,
        release=release,
        traces_sample_rate=float(os.getenv("SENTRY_TRACES_SAMPLE_RATE", "0.0")),
        profiles_sample_rate=float(os.getenv("SENTRY_PROFILES_SAMPLE_RATE", "0.0")),
        send_default_pii=False,
    )

    with sentry_sdk.configure_scope() as scope:
        scope.set_tag("app.name", app_name)
        scope.set_tag("host", socket.gethostname())
        scope.set_tag("cwd", os.getcwd())
        scope.set_extra("user", os.getenv("USERNAME") or os.getenv("USER"))


