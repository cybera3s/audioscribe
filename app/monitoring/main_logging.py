import logging

# local
from config import settings


stdout_log_path = settings.STDOUT_LOG_PATH
log_level = settings.LOG_LEVEL

LOGGING_MESSAGE_FORMAT = (
    "%(asctime)s - %(funcName)s - %(levelname)s: %(message)s"
)
LOGGING_DATE_FORMAT = "%d/%m/%y %H:%M:%S"


logging.basicConfig(
    filename=stdout_log_path,
    level=log_level,
    format=LOGGING_MESSAGE_FORMAT,
    datefmt=LOGGING_DATE_FORMAT,
)


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)
