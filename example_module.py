import custom_logger

logger = custom_logger.get_logger(__name__)

def process(msg):
    logger.info("Before the process")
    print(msg)
    logger.info("After the process")
