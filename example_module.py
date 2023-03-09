import custom_logger
from custom_logger import log_action

# logger = custom_logger.get_logger(__name__)
logger = custom_logger.init_action_log(__name__)


def process(msg):
    logger.info("Before the process")
    print(msg)
    log_action("some action", ["hello", 123])
    logger.info("some info log that is also action", action=True)
    logger.info("After the process")
