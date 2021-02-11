# Painless Logger for Python
 
A painless logging module for Python that enables logging to console and/or file.

Good primarily for debugging by default, but can be extended through the logging-config.yaml file for other use cases.


# Usage

```python
# Import all the available log message functions and assign them names.
from painless_logger.messages import console
INFO, WARNING, ERROR = console
from painless_logger.messages import file
INFO_FILE, WARNING_FILE, ERROR_FILE = file


# No additional set up or logger initialization necessary :)

INFO("This logs an info message.")
WARNING("This logs a warning message.")
WARNING_FILE("This logs a warning message to file.")

try:
    1/0
except:
    ERROR("This logs an error message. Use in except blocks, and a traceback will be added automatically.")

```
