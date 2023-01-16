from .loggingFunctions import log_debug, log_info, log_warning, log_error

class Result:
    def __init__(self, success: bool, message: str):
        self.success = success
        self.message = message

class UserInputError(Exception): 
    def __init__(self, message, vars=None):
        super().__init__(message)

        self.vars = vars
        if vars:
            print(message.format(vars))
            log_error(message.format(vars))
        else: 
            print(message)
            log_error(message)


# show functions only print the error/success
def showError(message: str, variable: str=None):
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

def showSuccess(message: str, variable: str=None):
    if variable:
        result = Result(success=True, message=message.format(variable))
    else:
        result = Result(success=True, message=message)
    # print and log the message
    print(result.message)

# return functions return the error/success tuple
def returnError(message: str, variable: str=None):
    if variable:
        result = Result(success=False, message=message.format(variable))
    else: 
        result = Result(success=False, message=message)
    # log and return error
    log_debug(result.message)
    return result

def returnSuccess(message: str, variable: str=None):
    if variable:
        result = Result(success=True, message=message.format(variable))
    else:
        result = Result(success=True, message=message)
    # log and return result
    log_info(result.message)
    return result