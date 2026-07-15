import logging
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)


logger = logging.getLogger("framework_logger")
logger.setLevel(logging.INFO)


def setup_test_logger(test_name):
    """
    Configures logger for current test.
    """

    # remove old handlers
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
        handler.close()

    log_file = LOG_DIR / f"{test_name}.log"

    file_handler = logging.FileHandler(
        log_file,
        mode="w"
    )

    console_handler = logging.StreamHandler()

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger