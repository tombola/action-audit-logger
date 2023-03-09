import logging
import inspect
from functools import cache

from objexplore import explore
from rich import print

# logging.basicConfig(level=logging.DEBUG)

_log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
_action_log_format = f"%(asctime)s - %(filename)s:%(lineno)d - %(message)s"

ACTION_TOKEN = "ACTION::"


def action_filter(record):
    # return record.levelno == logging.INFO
    # return record.levelno == logging.INFO and record.getMessage().startswith(ACTION_TOKEN)
    return record.levelno == logging.INFO and record.is_action


def get_file_handler():
    file_handler = logging.FileHandler("info.log")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(_log_format))
    return file_handler


def get_actions_file_handler():
    file_handler = logging.FileHandler("actions.log")
    file_handler.addFilter(action_filter)
    file_handler.setFormatter(logging.Formatter(_action_log_format))
    return file_handler


def get_stream_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(logging.Formatter(_log_format))
    return stream_handler


@cache
def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(get_file_handler())
    logger.addHandler(get_actions_file_handler())
    logger.addHandler(get_stream_handler())
    return logger


# logger = get_logger(__name__)

old_factory = logging.getLogRecordFactory()


def record_factory(*args, action=False, **kwargs):
    record = old_factory(*args, **kwargs)
    record.is_action = bool(action)
    return record


def init_action_log(name):
    logging.setLogRecordFactory(record_factory)
    return get_logger(__name__)


# TODO: instead of this function, use a custom log record factory?
# https://docs.python.org/3/library/logging.html#logging.setLogRecordFactory
# TODO: also see RotatingFileHandlers for per day logs
# https://gist.github.com/arduino12/144c346c9f3ecc8175be45a2f6bda599
# Also:
# https://github.com/madzak/python-json-logger
# https://pypi.org/project/dblogging
def log_action(message, object=None):
    calling_module = inspect.getmodule(inspect.stack()[1][0])
    logger = get_logger(calling_module.__name__)
    if not object:
        logger.info(f"{ACTION_TOKEN}{message}")
        return
    logger.info(f"{ACTION_TOKEN}{message} | {object}")
