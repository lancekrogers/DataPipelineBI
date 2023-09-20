import logging


def log_print(message, level="INFO"):
    log_levels = {
        "DEBUG": logging.debug,
        "INFO": logging.info,
        "WARNING": logging.warning,
        "ERROR": logging.error,
        "CRITICAL": logging.critical,
    }
    log_levels[level.upper()](message)
