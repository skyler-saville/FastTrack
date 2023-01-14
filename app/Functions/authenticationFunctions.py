from ..models import User
from .passwordFunctions import check_password

def login(session, email, password):
    user = session.query(User).filter_by(email=email).first()
    if user and check_password(password, user.password):
        # return tuple with format (Boolean, message)
        print("User logged in")
    else:
        print("Incorrect email or password")
