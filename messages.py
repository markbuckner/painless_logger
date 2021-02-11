import logging
import logging.config
import os
import yaml

class _PainlessLogger:
    """
    Simple logger using built-in Python logging library and YAML file for external config.

    A logging-config.yaml should be placed in your program's working directory. A default is provided.

    Logs to either console or file.
    """
    def __init__(self):
        try:
            # Read config from YAML file.
            with open('logging-config.yaml', 'rt') as configFile:
                config = yaml.safe_load(configFile.read())

                # Set logging config from dictionary.
                logging.config.dictConfig(config)

                # Get configured logger.
                self.file_logger = logging.getLogger('file')

                # Get configured logger.
                self.console_logger = logging.getLogger('console')

        except Exception as e:

            # Warn the user a file will be added.
            print("No logging-config.yaml found in the program's working directory.")
            print("PainlessLogger will attempt to add a default logging-config.yaml.")

            # If the logging-config.yaml file wasn't in the program's working directory,
            # then create the default logging config on the fly.
            default_config = \
"""
version: 1

formatters:
  simple:
    format: "%(asctime)s.%(msecs)03d\\t%(levelname)s\\t%(message)s"
    datefmt: '%m/%d/%Y %H:%M:%S'

  complex:
    format: "%(asctime)s.%(msecs)03d %(module)s.%(funcName)s() line-%(lineno)s %(threadName)s\\t%(levelname)s\\t%(message)s"
    datefmt: '%m/%d/%Y %H:%M:%S'

# Set loggers.
loggers:
  console:   
    level: DEBUG
    handlers: [console]

  file:
    level: DEBUG
    handlers: [file]

# Set logger handlers.
handlers:
  console:
    class: logging.StreamHandler
    stream: ext://sys.stdout
    level: DEBUG
    formatter: complex

  file:
    class: logging.FileHandler
    level: DEBUG
    formatter: complex
    # Use full file path for "filename".
    # If no path is provided, the log file gets placed in the program's working directory.
    filename: "DefaultLog.log"
               
"""
            try:
                # Write the default logging config to file in the current directory.
                with open('logging-config.yaml', 'w') as configFile:
                    configFile.write(default_config)

                # Read the file just written, and initialize loggers.
                with open('logging-config.yaml', 'r') as configFile:
                    config = yaml.safe_load(configFile.read())

                    # Set logging config from dictionary.
                    logging.config.dictConfig(config)

                    # Get configured logger.
                    self.file_logger = logging.getLogger('file')

                    # Get configured logger.
                    self.console_logger = logging.getLogger('console')

            except Exception as e:
                raise RuntimeError("Unable to create config file in working directory.")

    def __del__(self):
        # If the file log was empty, delete it.
        # The destructor isn't guaranteed to be called. So this cleanup isn't guaranteed.
        if os.stat("DefaultLog.log").st_size == 0:
            os.remove('DefaultLog.log')


# Initialize the default logger and message functions for even easier, lazier importing.
_PainlessLogger = _PainlessLogger()

# Info log message function.
INFO = _PainlessLogger.console_logger.info

# Warning log message function.
WARNING = _PainlessLogger.console_logger.warning

# Error log message function
ERROR = _PainlessLogger.console_logger.exception

console = INFO, WARNING, ERROR

# Info file log message function.
INFO_FILE = _PainlessLogger.file_logger.info

# Warning file log message function.
WARNING_FILE = _PainlessLogger.file_logger.warning

# Error file log message function.
ERROR_FILE = _PainlessLogger.file_logger.exception

file = INFO, WARNING, ERROR
