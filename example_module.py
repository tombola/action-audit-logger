import custom_logger
from custom_logger import log_action

logger = custom_logger.get_logger(__name__)


def process(msg):
    logger.info("Before the process")
    print(msg)
    log_action("some action", ["hello", 123])
    logger.info("After the process")
