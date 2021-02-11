# Demo of how to import and use the logger.

# Import all the available log message functions and assign them names.
from painless_logger.messages import console
INFO, WARNING, ERROR = console
from painless_logger.messages import file
INFO_FILE, WARNING_FILE, ERROR_FILE = file


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
