# Use this file to create new users, chores, rewards, punishments
from datetime import datetime
from .errorHandlerFunctions import showError, showSuccess, returnError, returnSuccess
from .passwordFunctions import hash_password
from ..models import User, Chore, Reward, Punishment



# CREATE A NEW USER
def create_user(session, username, password, email, userRole, balance=0.0):
    roles = ['child', 'parent']
    existingUser = session.query(User).filter_by(email=email).first()
    if existingUser:
        # if user exists, return a tuple with format (Boolean, message)
        returnError('User with email "{}" already exists', email)   
    # add an if statement to check if user_role is equal to "parent" or "child"
    if userRole in roles:
        hashedPassword = hash_password(password)
        new_user = User(username=username.casefold(), password=hashedPassword, email=email.casefold(), 
                    created_on=datetime.now(), user_role=userRole.casefold(), balance=balance)
        session.add(new_user)
        session.commit()
        # upon successful user creation, return tuple with format (Boolean, message)
        showSuccess('new user added: {}', username)
        returnSuccess('User with email "{}" created', email)
    else:
        showError('User could not be created. The "{}" role does not exist', userRole)
        returnError('The "{}" role does not exist', userRole)
        

# CREATE A NEW CHORE
def create_chore(session, choreName, description, amount):
    # do something
    new_chore = Chore(chore_name=choreName.casefold(), description=description.capitalize(), amount=amount, created_on=datetime.now())
    session.add(new_chore)
    showSuccess('new chore added: {}', choreName)
    session.commit()


# CREATE A NEW REWARD
def create_reward(session, rewardName, description, amount):
    new_reward = Reward(reward_name=rewardName.casefold(), description=description.capitalize(), amount=amount, created_on=datetime.now())
    session.add(new_reward)
    showSuccess('new reward added: {}', rewardName)
    session.commit()

# CREATE A NEW PUNISHMENT
def create_punishment(session, punishmentName, description, amount):
    new_punishment = Punishment(punishment_name=punishmentName.casefold(), description=description.capitalize(), amount=amount, created_on=datetime.now())
    session.add(new_punishment)
    showSuccess('new punishment added: {}', punishmentName)
    session.commit()

