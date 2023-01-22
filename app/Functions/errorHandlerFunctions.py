# from .loggingFunctions import log_debug, log_info, log_warning, log_error
from ..logs.loggers import log_info, log_debug, log_warning, log_error
import json

class Result:
    def __init__(self, success: bool, message: str):
        self.success = success
        self.message = message

class UserInputError(Exception): 
    """
        Exception raised during user creation, if any data submitted 
        doesn't pass the validation checks
    """
    def __init__(self, message: dict, data: dict=None):
        self.message = message
        self.data = data
        super().__init__(message)

        self.data = data
        if data:
            if 'warning' in data.values():
                print(f'warning in data.values: {data.values()}')
                log_warning({json.dumps(message), json.dumps(data)})
            else:
                print(f'UserInputError exception raised (with data:{data})')
                log_error({json.dumps(message), json.dumps(data)})
        else: 
            print(f'UserInputError exception raised: {message}')
            log_error(json.dumps(message))


# show functions only print the error/success
def showError(message: str, variable: str=None) -> None:
    if variable:
        result = Result(success=False, message=message.format(variable))
    else: 
        result = Result(success=False, message=message)
    # print and log the error
    print(result.message)
    log_error(result.message)

def showException(message: str, variable: str=None): # use this inside try block
    # use 'raise UserInputError(showException('some message for {}', error))
    if variable:
        result = message.format(variable)
    else:
        result = message
    return result

def showSuccess(message: str, variable: str=None) -> None:
    if variable:
        result = Result(success=True, message=message.format(variable))
    else:
        result = Result(success=True, message=message)
    # print and log the message
    print(result.message)

# return functions return the error/success tuple
def returnError(message: str, variable: str=None) -> Result:
    if variable:
        result = Result(success=False, message=message.format(variable))
    else: 
        result = Result(success=False, message=message)
    # log and return error
    log_debug(result.message)
    return result

def returnSuccess(message: str, variable: str=None) -> Result:
    if variable:
        result = Result(success=True, message=message.format(variable))
    else:
        result = Result(success=True, message=message)
    # log and return result
    log_info(result.message)
    return result