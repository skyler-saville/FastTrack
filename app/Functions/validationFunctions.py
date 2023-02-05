import re

def valid_email(email):
    pattern = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
    return pattern.match(email)

def valid_username(username):
    # Minimum 3 characters consisting of letters, numbers, hyphens, underscores
    # Username is not the unique identifier for the system... only for the family group
    # so there can/will be duplicates in the system. 
    # As long as the user has a valid and unique email, that's all that matters
    pattern = re.match("^[a-zA-Z0-9_-]{3,15}$", username)
    return pattern

def valid_password(password):
    # Minimum eight characters, at least one letter and one number
    pattern = re.match("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", password)
    return pattern