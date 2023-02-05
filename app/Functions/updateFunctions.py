from datetime import datetime
from .errorHandlerFunctions import showError, showSuccess, returnError, returnSuccess
from .passwordFunctions import hash_password, check_password
from .validationFunctions import valid_email
from ..models import User, Chore, Reward, Punishment


# UPDATE A USER
def update_user(session, user_id, username=None, email=None, password=None):
    validUser = True
    try:
        user = session.query(User).filter_by(user_id=user_id).first()
    except Exception as e:
        validUser = False
        returnError('Database error: {}', e.args)

    if user is None:
        validUser = False
        returnError('User with ID "{}" not found.', user_id)
   
    if validUser:
        try:
            if username:
                user.username = username
            if email:
                if valid_email(email):
                    user.email = email
                else:
                    returnError('Email "{}" submitted was not in valid format', email)
            if password:
                if check_password(password, user.password):
                    returnError('User password matches existing password')
                else:
                    user.password = hash_password(password)
            # set edited_on 
            user.edited_on = datetime.now()

        except Exception as e:
            # rollback any changes to the database if there was an error
            session.rollback()
            showError('Unable to update user with id: {}', user_id)
            returnError('Database error: {}', e.args)

        # moved the commits to outside the try blocks
        # Commit update to database if there are no Exceptions
        session.commit()
        showSuccess('User with ID "{}" was successfully updated.', user_id)
        returnSuccess('User with ID "{}" was updated.', user_id)

    else:
        showError('Server rejected request to update user with ID "{}".', user_id)
        returnError('Server rejected request to update user with ID "{}".', user_id)


# UPDATE A CHORE
def update_chore(session, chore_id, chore_name=None, description=None, amount=None):
    validChore = True
    try:
        chore = session.query(Chore).filter_by(chore_id=chore_id).first()
    except Exception as e:
        validChore = False
        returnError('Database error: {}', e.args)
        
    if chore is None:
        validChore = False
        returnError('Chore with ID "{}" not found.', chore_id)
        
    if validChore:
        try:
            if chore_name:
                chore.chore_name = chore_name.casefold()
            if description:
                chore.description = description.capitalize()
            if amount:
                chore.amount = amount
            # set edited_on 
            chore.edited_on = datetime.now()

        except Exception as e:
            session.rollback()
            returnError('Database error: {}', e.args)

        # Commit update to database if there are no Exceptions
        session.commit()
        showSuccess('Chore with ID "{}" was successfully updated.', chore_id)
        returnSuccess('Chore with ID "{}" was updated.', chore_id)

    else:
        showError('Server rejected request to update chore with ID "{}".', chore_id)
        returnError('Server rejected request to update chore with ID "{}".', chore_id)


# UPDATE A REWARD
def update_reward(session, reward_id, reward_name=None, description=None, amount=None):
    validReward = True
    try:
        reward = session.query(Reward).filter_by(id=reward_id).first()
    except Exception as e: 
        validReward = False
        returnError('Database error: {}', e.args)

    if reward is None:
        validReward = False
        returnError('Reward with ID "{}" not found.', reward_id)

    if validReward:
        try:
            if reward_name:
                reward.reward_name = reward_name.casefold()
            if description:
                reward.description = description.capitalize()
            if amount:
                reward.amount = amount
            # set edited_on 
            reward.edited_on = datetime.now()

        except Exception as e:
            session.rollback()
            showError('Unable to update reward with id: {}', reward_id)
            returnError('Database error: {}', e.args)

        # Commit update to database if there are no Exceptions
        session.commit()
        showSuccess('Reward with ID "{}" was successfully updated.', reward_id)
        returnSuccess('Reward with ID "{}" was updated.', reward_id)

    else:
        showError('Server rejected request to update reward with ID "{}".', reward_id)
        returnError('Server rejected request to update reward with ID "{}".', reward_id)


# UPDATE A PUNISHMENT
def update_punishment(session, punishment_id, punishment_name=None, description=None, amount=None):
    validPunishment = True
    try:
        punishment = session.query(Punishment).filter_by(punishment_id=punishment_id).first()
    except Exception as e:
        validPunishment = False
        returnError('Database error: {}', e.args)

    if punishment is None:
        validPunishment = False
        returnError('Punishment with ID "{}" not found.', punishment_id)

    if validPunishment:
        try:
            if punishment_name:
                punishment.punishment_name = punishment_name
            if description:
                punishment.description = description
            if amount:
                punishment.amount = amount
            # set edited_on 
            punishment.edited_on = datetime.now()

        except Exception as e:
            session.rollback()
            showError('Unable to update punishment with id: {}', punishment_id)
            returnError('Database error: {}', e.args)

        # Commit update to database if there are no Exceptions
        session.commit()
        showSuccess('Punishment with ID "{}" was successfully updated.', punishment_id)
        returnSuccess('Punishment with ID "{}" was updated.', punishment_id)

    else:
        showError('Server rejected request to update punishment with ID "{}".', punishment_id)
        returnError('Server rejected request to update punishment with ID "{}".', punishment_id)
