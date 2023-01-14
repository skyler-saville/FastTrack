import bcrypt

def check_password(plain_text_password, hashed_password):
    # compare the plain-text password to the hashed password
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_password)

def hash_password(password):
    # Number of salt rounds
    rounds = 12
    # Generate a unique salt
    salt = bcrypt.gensalt(rounds)
    # hash the plain-text password
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    # return the hashed/salted password
    return hashed