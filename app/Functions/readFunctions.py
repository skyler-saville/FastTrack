from .errorHandlerFunctions import showError, showSuccess, returnError, returnSuccess
from ..models import User, Chore, Reward, Punishment

# RETRIEVE ONE USER BY ID
def read_user(session, user_id):
    try:
        user = session.query(User).filter_by(id=user_id).first()
        if user:
            showSuccess('User with ID "{}" found.', user_id)
            returnSuccess(user)
        else:
            showError('No user found with ID "{}".', user_id)
            returnError('No user found with ID "{}".', user_id)
    except Exception as e:
        returnError('Database error: {}', e.args)

# RETRIEVE ALL USERS
def read_users(session):
    try:
        users = session.query(User).all()
        if users:
            showSuccess('All Users retrieved.')
            returnSuccess(users)
        else:
            showError('No Users found.')
            returnError('No Users found.')
    except Exception as e:
        returnError('Database error: {}', e.args)


# RETRIEVE ONE CHORE BY ID
def read_chore(session, chore_id):
    try:
        chore = session.query(Chore).filter_by(id=chore_id).first()
        if chore:
            showSuccess('Chore with ID "{}" found.', chore_id)
            returnSuccess(chore)
        else:
            showError('No chore found with ID "{}".', chore_id)
            returnError('No chore found with ID "{}".', chore_id)
    except Exception as e:
        returnError('Database error: {}', e.args)


# RETRIEVE ALL CHORES
def read_chores(session):
    try:
        chores = session.query(Chore).all()
        if chores:
            showSuccess('All Chores retrieved.')
            returnSuccess(chores)
        else:
            showError('No Chores found.')
            returnError('No Chores found.')
    except Exception as e:
        returnError('Database error: {}', e.args)


# RETRIEVE ONE REWARD BY ID
def read_reward(session, reward_id):
    try:
        reward = session.query(Reward).filter_by(id=reward_id).first()
        if reward:
            showSuccess('Reward with ID "{}" found.', reward_id)
            returnSuccess(reward)
        else:
            showError('No reward found with ID "{}".', reward_id)
            returnError('No reward found with ID "{}".', reward_id)
    except Exception as e:
        returnError('Database error: {}', e.args)


# RETRIEVE ALL REWARDS
def read_rewards(session):
    try:
        rewards = session.query(Reward).all()
        if rewards:
            showSuccess('All Rewards retrieved.')
            returnSuccess(rewards)
        else:
            showError('No Rewards found.')
            returnError('No Rewards found.')
    except Exception as e:
        returnError('Database error: {}', e.args)


# RETRIEVE ONE PUNISHMENT BY ID
def read_punishment(session, punishment_id):
    try:
        punishment = session.query(Punishment).filter_by(id=punishment_id).first()
        if punishment:
            showSuccess('Punishment with ID "{}" found.', punishment_id)
            returnSuccess(punishment)
        else:
            showError('No punishment found with ID "{}".', punishment_id)
            returnError('No punishment found with ID "{}".', punishment_id)
    except Exception as e:
        returnError('Database error: {}', e.args)


# RETRIEVE ALL PUNISHMENTS
def read_punishments(session):
    try:
        punishments = session.query(Punishment).all()
        if punishments:
            showSuccess('All Punishments retrieved.')
            returnSuccess(punishments)
        else:
            showError('No Punishments found.')
            returnError('No Punishments found.')
    except Exception as e:
        returnError('Database error: {}', e.args)