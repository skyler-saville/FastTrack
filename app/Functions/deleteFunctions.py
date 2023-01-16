from .errorHandlerFunctions import showError, showSuccess, returnError, returnSuccess
from ..models import User, Chore, Reward, Punishment

# DELETE A USER
def delete_user(session, user_id):
    validUser = True
    try:
        user = session.query(User).filter_by(id=user_id).first()
    except Exception as e:
        validUser = False
        returnError('Database error: {}', e.args)

    if user is None:
        validUser = False
        returnError('User with ID "{}" not found.', user_id)
   
    if validUser:
        try:
            session.delete(user)
            session.commit()
            showSuccess('User with ID "{}" was successfully deleted.', user_id)
            returnSuccess('User with ID "{}" was deleted.', user_id)
        except Exception as e:
            showError('Unable to delete user with id: {}', user_id)
            returnError('Database error: {}', e.args)

    else:
        showError('Server rejected request to delete user with ID "{}".', user_id)
        returnError('Server rejected request to delete user with ID "{}".', user_id)


# DELETE A CHORE
def delete_chore(session, chore_id):
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
            session.delete(chore)
            session.commit()
            showSuccess('Chore with ID "{}" was successfully deleted.', chore_id)
            returnSuccess('Chore with ID "{}" was deleted.', chore_id)
        except Exception as e:
            showError('Unable to delete chore with id: {}', chore_id)
            returnError('Database error: {}', e.args)

    else:
        showError('Server rejected request to delete chore with ID "{}".', chore_id)
        returnError('Server rejected request to delete chore with ID "{}".', chore_id)


# DELETE A REWARD
def delete_reward(session, reward_id):
    validReward = True
    try:
        reward = session.query(Reward).filter_by(reward_id=reward_id).first()
    except Exception as e: 
        validReward = False
        returnError('Database error: {}', e.args)

    if reward is None:
        validReward = False
        returnError('Reward with ID "{}" not found.', reward_id)

    if validReward:
        try:
            session.delete(reward)
            session.commit()
            showSuccess('Reward with ID "{}" was successfully deleted.', reward_id)
            returnSuccess('Reward with ID "{}" was deleted.', reward_id)
        except Exception as e:
            showError('Unable to delete reward with id: {}', reward_id)
            returnError('Database error: {}', e.args)

    else:
        showError('Server rejected request to delete reward with ID "{}".', reward_id)
        returnError('Server rejected request to delete reward with ID "{}".', reward_id)

# DELETE A PUNISHMENT
def delete_punishment(session, punishment_id):
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
            session.delete(punishment)
            session.commit()
            showSuccess('Punishment with ID "{}" was successfully deleted.', punishment_id)
            returnSuccess('Punishment with ID "{}" was deleted.', punishment_id)
        except Exception as e:
            showError('Unable to delete punishment with id: {}', punishment_id)
            returnError('Database error: {}', e.args)

    else:
        showError('Server rejected request to delete punishment with ID "{}".', punishment_id)
        returnError('Server rejected request to delete punishment with ID "{}".', punishment_id)