import logging
from pythonjsonlogger import jsonlogger


# THESE WERE ALL PRIOR TO ADDING THE JSONLOGGER
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

# file_handler = logging.FileHandler('errors.log')
# file_handler.setLevel(logging.WARNING) # Log only Warnings, Errors or Exceptions

# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)

# logger.addHandler(file_handler)



# logger = logging.getLogger()

formatter = jsonlogger.JsonFormatter('%(asctime)s - %(levelname)s - %(message)s')
json_handler = logging.FileHandler(filename='./app/logs/errors.json')
json_handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(json_handler)

def log_debug(message: dict):
    print('Logging debug message...')
    logger.debug(message)

def log_info(message: dict):
    print('Logging info message...')
    logger.info(message)

def log_warning(message: dict):
    print('Logging warning message...')
    logger.warning(message)

def log_error(message: dict, exception=None):
    if exception:
        print('Logging exception message...')
        logger.exception(message, exc_info=exception)
    else:
        print('Logging error message...')
        logger.error(message)

# Usage
log_debug({"message":"Initial log debug test"})
log_info({"message":"Initial log info test"})
log_warning({"message":"Initial log warning test"})
log_error({"message":"Initial log error test"})

# logger.removeHandler(file_handler) 
