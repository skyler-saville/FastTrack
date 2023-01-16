# Use this file to create new users, chores, rewards, punishments
from datetime import datetime
from .errorHandlerFunctions import showError, showSuccess, returnError, returnSuccess, UserInputError, showException
from .passwordFunctions import hash_password
from .validationFunctions import valid_email
from ..models import User, Chore, Reward, Punishment



# CREATE A NEW USER
def create_user(session, username, password, email, userRole, balance=0.0):
    roles = ['child', 'parent']
    validUser = True
    reason = None
    existingUser = session.query(User).filter_by(email=email).first()
    try:
        if not isinstance(balance, float):
            validUser = False
            reason = 'Balance not Float'
            raise UserInputError('balance not a float')
        
        if balance < -99999.99 or balance > 99999.99:
            validUser = False
            reason = 'Balance < -99999.99 or > 99999.99'
            raise UserInputError('number of digits in balance exceed valid amount')

        if existingUser:
            validUser = False
            reason = 'User/email already in database'
            raise UserInputError('User with email "{}" already exists', email)
        
        if userRole not in roles:
            validUser = False
            reason = 'Role was not either "child" or "parent"'
            raise UserInputError('User cannot have assigned role of {}', userRole)
        
        if not valid_email(email):
            validUser = False
            reason = 'No valid email address was given'
            raise UserInputError('Users supplied email {} is not valid', email)
    except UserInputError as e: 
            showError(e)
    
    if validUser:
        hashedPassword = hash_password(password)
        new_user = User(username=username.casefold(), password=hashedPassword, email=email.casefold(), 
                    created_on=datetime.now(), user_role=userRole.casefold(), balance=balance)
        session.add(new_user)
        session.commit()
        # upon successful user creation, return tuple with format (Boolean, message)
        showSuccess('new user added: {}', username)
        return returnSuccess('User with email "{}" created', email)
    
    else:
        showError('Server rejected request to create new user "{}".', username)
        
        return returnError('Server rejected request: {}', reason)
        

# CREATE A NEW CHORE
def create_chore(session, choreName, description, amount):
    # check if choreName already exists
    validChore = True
    try:
        existingChore = session.query(Chore).filter_by(chore_name=choreName).first()
    except Exception as e:
        return returnError('Database error: {}', e.args)

    if session is None:
        validChore = False
        return returnError('Chore not created, no database session exists')
    
    if existingChore:
        validChore = False
        return returnError('Chore "{}" already exists', choreName)

    if choreName is None:
        validChore = False
        return returnError('Chore Name required')
    
    if len(choreName) > 50:
        validChore = False
        return returnError('Chore name must be less than 50 characters')

    if description is None:
        validChore = False
        return returnError('Chore Description required.')
    
    if len(description) > 100:
        validChore = False
        return returnError('Chore Description must be less than 100 characters')

    if (amount <= 0):
        validChore = False
        return returnError('Chore amount must positive')
    
    if validChore:
        try:
            new_chore = Chore(chore_name=choreName.casefold(), description=description.capitalize(), amount=amount, created_on=datetime.now())
            session.add(new_chore)
            session.commit()
            showSuccess('Chore "{}" was successfully created.', choreName)
            return returnSuccess('Chore "{}" was created.', choreName)
        except Exception as e:
            return returnError('Database error: {}', e.args)

    else:
        showError('Server rejected request to create new chore "{}"', choreName)
        return returnError('Server rejected request to create new chore "{}"', choreName)



# CREATE A NEW REWARD
def create_reward(session, rewardName, description, amount):
    # Set the default of 'validReward' to True, then run it against the different validations
    validReward = True
    try:
        existingReward = session.query(Reward).filter_by(reward_name=rewardName).first()
    except Exception as e:
        return returnError('Database error: {}', e.args)
    # check session 
    if session is None:
        validReward = False
        return returnError('Reward not created, no database session exists')
    # check if already exists
    if existingReward:
        validReward = False
        return returnError('Reward "{}" already exists', rewardName)
    # validate name exists
    if rewardName is None:
        validReward = False
        return returnError('Reward Name required')
    # validate name length less than 50
    if len(rewardName) > 50:
        validReward = False
        return returnError('Reward name must be less than 50 characters')
    # validate description exists
    if description is None:
        validReward = False
        return returnError('Reward Description required.')
    # validate description length less than 100
    if len(description) > 100:
        validReward = False
        return returnError('Reward Description must be less than 100 characters')
    # validate reward amount is less than 0
    if (amount >= 0):
        validReward = False
        return returnError('Reward amount must be negative')
    # if reward is valid, create the reward in the database
    if validReward:
        try:
            new_reward = Reward(reward_name=rewardName.casefold(), description=description.capitalize(), amount=amount, created_on=datetime.now())
            session.add(new_reward)
            session.commit()
            showSuccess('Reward "{}" was successfully created.', rewardName)
            return returnSuccess('Reward "{}" was created.', rewardName)
        except Exception as e:
            return returnError('Database error: {}', e.args)
    else:
        showError('Server rejected request to create new reward "{}"', rewardName)
        return returnError('Server rejected request to create new reward "{}"', rewardName)


# CREATE A NEW PUNISHMENT
def create_punishment(session, punishmentName, description, amount):
    # check if punishmentName already exists
    validPunishment = True
    try:
        existingPunishment = session.query(Punishment).filter_by(punishment_name=punishmentName).first()
    except Exception as e:
        return returnError('Database error: {}', e.args)

    if session is None:
        validPunishment = False
        return returnError('Punishment not created, no database session exists')
    
    if existingPunishment:
        validPunishment = False
        return returnError('Punishment "{}" already exists', punishmentName)

    if punishmentName is None:
        validPunishment = False
        return returnError('Punishment Name required')
    
    if len(punishmentName) > 50:
        validPunishment = False
        return returnError('Punishment name must be less than 50 characters')

    if description is None:
        validPunishment = False
        return returnError('Punishment Description required.')
    
    if len(description) > 100:
        validPunishment = False
        return returnError('Punishment Description must be less than 100 characters')

    if (amount >= 0):
        validPunishment = False
        return returnError('Punishment amount must negative')
    
    if validPunishment:
        try:
            new_punishment = Punishment(punishment_name=punishmentName.casefold(), description=description.capitalize(), amount=amount, created_on=datetime.now())
            session.add(new_punishment)
            session.commit()
            showSuccess('Punishment "{}" was successfully created.', punishmentName)
            return returnSuccess('Punishment "{}" was created.', punishmentName)
        except Exception as e:
            return returnError('Database error: {}', e.args)

    else:
        showError('Server rejected request to create new punishment "{}"', punishmentName)
        return returnError('Server rejected request to create new punishment "{}"', punishmentName)


