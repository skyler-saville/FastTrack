# Setup a class to allow using 
class Result:
    def __init__(self, success: bool, message: str):
        self.success = success
        self.message = message.capitalize()

# show functions only print the error/success
def showError(message: str, variable: str=None):
    if variable:
        result = Result(success=False, message=message.format(variable))
        print(result.message)
    else: 
        result = Result(success=False, message=message)
        print(result.message)

def showSuccess(message: str, variable: str=None):
    if variable:
        result = Result(success=True, message=message.format(variable))
        print(result.message)
    else:
        result = Result(success=True, message=message)
        print(result.message)

# return functions return the error/success tuple
def returnError(message: str, variable: str=None):
    if variable:
        return Result(success=False, message=message.format(variable))
    else: 
        return Result(success=False, message=message)

def returnSuccess(message: str, variable: str=None):
    if variable:
        return Result(success=True, message=message.format(variable))
    else:
        return Result(success=True, message=message)