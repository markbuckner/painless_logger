# painless_logger
 
A painless logging module for Python. 

Ready to log to console and file after just import statements. No initialization or additional scaffolding code required. 

Good primarily for debugging by default, but can be extended through the logging-config.yaml file for other use cases.


# Usage

```python
# Import all the default available log message functions.

# Console log message functions.
from painless_logger.messages import INFO
from painless_logger.messages import WARNING
from painless_logger.messages import ERROR

# File log message functions.
from painless_logger.messages import INFO_FILE
from painless_logger.messages import WARNING_FILE
from painless_logger.messages import ERROR_FILE

# No additional set up or logger initialization necessary :)

INFO("This logs an info message.")
WARNING("This logs a warning message.")
WARNING_FILE("This logs a warning message to file.")

try:
    1/0
except:
    ERROR("This logs an error message. Use the error message in except blocks, and a traceback will be added automatically to the message.")


```
