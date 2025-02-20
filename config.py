import os
import sys
import logging


logger = logging.getLogger(__name__)


def get_app_url() -> str:
    """Return the OTEL demo url."""
    app_url = os.environ.get("OTEL_DEMO_APP_URL")
    if app_url is None:
        logger.error("OTEL_DEMO_APP_URL is missing")
        sys.exit(1)
    return app_url
