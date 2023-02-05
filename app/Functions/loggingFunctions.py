# import logging


# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)

# file_handler = logging.FileHandler('app.log')
# file_handler.setLevel(logging.WARNING) # Log only Warnings, Errors or Exceptions

# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)

# logger.addHandler(file_handler)

# def log_debug(message: str):
#     print('Logging debug message...')
#     logger.debug(message)

# def log_info(message: str):
#     print('Logging info message...')
#     logger.info(message)

# def log_warning(message: str):
#     print('Logging warning message...')
#     logger.warning(message)

# def log_error(message: str, exception=None):
#     if exception:
#         print('Logging exception message...')
#         logger.exception(message, exc_info=exception)
#     else:
#         print('Logging error message...')
#         logger.error(message)

# # Usage
# log_debug("Initial log debug test")
# log_info("Initial log info test")
# log_warning("Initial log warning test")
# log_error("Initial log error test")

# # logger.removeHandler(file_handler) 
