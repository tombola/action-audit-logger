"""
Example from '8 Advanced Python Logging Features that You Shouldn't Miss'
https://towardsdatascience.com/8-advanced-python-logging-features-that-you-shouldnt-miss-a68a5ef1b62d
"""

import example_module
import custom_logger

logger = custom_logger.get_logger(__name__)
# logger = custom_logger.logger

def main():
    logger.info("START")
    example_module.process(msg="a_message")
    logger.warning("This should appear in both console and log file")
    logger.info("FINISH")

if __name__ == "__main__":
    main()