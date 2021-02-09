# Demo of how to import and use the logger.

# Import all the available log message functions.

# Console log message functions.
from painless_logger.messages import INFO
from painless_logger.messages import WARNING
from painless_logger.messages import ERROR

# File log message functions.
from painless_logger.messages import INFO_FILE
from painless_logger.messages import WARNING_FILE
from painless_logger.messages import ERROR_FILE


def main():

    INFO("Hello info.")
    WARNING("Hello warning.")

    try:
        1/0
    except Exception:
        ERROR("Hello error. A traceback will be added on the next line automatically: ")

    INFO_FILE("Hello info.")
    WARNING_FILE("Hello warning.")

    try:
        1 / 0
    except Exception:
        ERROR_FILE("Hello error. A traceback will be added on the next line automatically: ")


# Calls main.
if __name__ == '__main__':
    main()
