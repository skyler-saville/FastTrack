# Use this file to create new users, chores, rewards, punishments
from datetime import datetime
from .errorHandlerFunctions import showError, showSuccess, returnError, returnSuccess
from .passwordFunctions import hash_password
from .validationFunctions import valid_email
from ..models import User, Chore, Reward, Punishment



# CREATE A NEW USER
def create_user(session, username, password, email, userRole, balance=0.0):
    roles = ['child', 'parent']
    validUser = True
    existingUser = session.query(User).filter_by(email=email).first()
    
    if existingUser:
        validUser = False
        returnError('User with email "{}" already exists', email)   
    
    if userRole not in roles:
        validUser = False
        returnError('User cannot have assigned role of {}', userRole)
    
    if not valid_email(email):
        validUser = False
        returnError('Users supplied email {} is not valid', email)
    
    if validUser:
        hashedPassword = hash_password(password)
        new_user = User(username=username.casefold(), password=hashedPassword, email=email.casefold(), 
                    created_on=datetime.now(), user_role=userRole.casefold(), balance=balance)
        session.add(new_user)
        session.commit()
        # upon successful user creation, return tuple with format (Boolean, message)
        showSuccess('new user added: {}', username)
        returnSuccess('User with email "{}" created', email)
    
    else:
        showError('Server rejected request to create new user "{}".', username)
        returnError('Server rejected request to create new user "{}".', username)
        

# CREATE A NEW CHORE
def create_chore(session, choreName, description, amount):
    # check if choreName already exists
    validChore = True
    try:
        existingChore = session.query(Chore).filter_by(chore_name=choreName).first()
    except Exception as e:
        returnError('Database error: {}', e.args)

    if session is None:
        validChore = False
        returnError('Chore not created, no database session exists')
    
    if existingChore:
        validChore = False
        returnError('Chore "{}" already exists', choreName)

    if choreName is None:
        validChore = False
        returnError('Chore Name required')
    
    if len(choreName) > 50:
        validChore = False
        returnError('Chore name must be less than 50 characters')

    if description is None:
        validChore = False
        returnError('Chore Description required.')
    
    if len(description) > 100:
        validChore = False
        returnError('Chore Description must be less than 100 characters')

    if (amount <= 0):
        validChore = False
        returnError('Chore amount must positive')
    
    if validChore:
        try:
            new_chore = Chore(chore_name=choreName.casefold(), description=description.capitalize(), amount=amount, created_on=datetime.now())
            session.add(new_chore)
            session.commit()
            showSuccess('Chore "{}" was successfully created.', choreName)
            returnSuccess('Chore "{}" was created.', choreName)
        except Exception as e:
            returnError('Database error: {}', e.args)

    else:
        showError('Server rejected request to create new chore "{}"', choreName)
        returnError('Server rejected request to create new chore "{}"', choreName)



# CREATE A NEW REWARD
def create_reward(session, rewardName, description, amount):
    # Set the default of 'validReward' to True, then run it against the different validations
    validReward = True
    try:
        existingReward = session.query(Reward).filter_by(reward_name=rewardName).first()
    except Exception as e:
        returnError('Database error: {}', e.args)
    # check session 
    if session is None:
        validReward = False
        returnError('Reward not created, no database session exists')
    # check if already exists
    if existingReward:
        validReward = False
        returnError('Reward "{}" already exists', rewardName)
    # validate name exists
    if rewardName is None:
        validReward = False
        returnError('Reward Name required')
    # validate name length less than 50
    if len(rewardName) > 50:
        validReward = False
        returnError('Reward name must be less than 50 characters')
    # validate description exists
    if description is None:
        validReward = False
        returnError('Reward Description required.')
    # validate description length less than 100
    if len(description) > 100:
        validReward = False
        returnError('Reward Description must be less than 100 characters')
    # validate reward amount is less than 0
    if (amount >= 0):
        validReward = False
        returnError('Reward amount must be negative')
    # if reward is valid, create the reward in the database
    if validReward:
        try:
            new_reward = Reward(reward_name=rewardName.casefold(), description=description.capitalize(), amount=amount, created_on=datetime.now())
            session.add(new_reward)
            session.commit()
            showSuccess('Reward "{}" was successfully created.', rewardName)
            returnSuccess('Reward "{}" was created.', rewardName)
        except Exception as e:
            returnError('Database error: {}', e.args)
    else:
        showError('Server rejected request to create new reward "{}"', rewardName)
        returnError('Server rejected request to create new reward "{}"', rewardName)


# CREATE A NEW PUNISHMENT
def create_punishment(session, punishmentName, description, amount):
    # check if punishmentName already exists
    validPunishment = True
    try:
        existingPunishment = session.query(Punishment).filter_by(punishment_name=punishmentName).first()
    except Exception as e:
        returnError('Database error: {}', e.args)

    if session is None:
        validPunishment = False
        returnError('Punishment not created, no database session exists')
    
    if existingPunishment:
        validPunishment = False
        returnError('Punishment "{}" already exists', punishmentName)

    if punishmentName is None:
        validPunishment = False
        returnError('Punishment Name required')
    
    if len(punishmentName) > 50:
        validPunishment = False
        returnError('Punishment name must be less than 50 characters')

    if description is None:
        validPunishment = False
        returnError('Punishment Description required.')
    
    if len(description) > 100:
        validPunishment = False
        returnError('Punishment Description must be less than 100 characters')

    if (amount >= 0):
        validPunishment = False
        returnError('Punishment amount must negative')
    
    if validPunishment:
        try:
            new_punishment = Punishment(punishment_name=punishmentName.casefold(), description=description.capitalize(), amount=amount, created_on=datetime.now())
            session.add(new_punishment)
            session.commit()
            showSuccess('Punishment "{}" was successfully created.', punishmentName)
            returnSuccess('Punishment "{}" was created.', punishmentName)
        except Exception as e:
            returnError('Database error: {}', e.args)

    else:
        showError('Server rejected request to create new punishment "{}"', punishmentName)
        returnError('Server rejected request to create new punishment "{}"', punishmentName)


