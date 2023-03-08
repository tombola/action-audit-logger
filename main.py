"""
Example from '8 Advanced Python Logging Features that You Shouldn't Miss'
https://towardsdatascience.com/8-advanced-python-logging-features-that-you-shouldnt-miss-a68a5ef1b62d
"""

import example_module
import custom_logger

logger = custom_logger.get_logger(__name__)

def main():
    logger.info("Program starts")
    example_module.process(msg="a_message")
    logger.warning("This should appear in both console and log file")
    logger.info("Program is over")

if __name__ == "__main__":
    main()