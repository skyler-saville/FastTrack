# Use this file to create new users, chores, rewards, punishments
from datetime import datetime
from ..models import User, Chore, Reward, Punishment

# CREATE A NEW USER
def create_user(session, username, password, email, user_role, balance=0.0):
    new_user = User(username=username, password=password, email=email, 
                    created_on=datetime.now(), user_role=user_role, balance=balance)
    session.add(new_user)
    print('new user added: {}'.format(username))
    session.commit()


# CREATE A NEW CHORE
def create_chore(session, choreName, description, amount):
    # do something
    new_chore = Chore(chore_name=choreName, description=description, amount=amount)
    session.add(new_chore)
    print('new chore added: {}'.format(choreName))
    session.commit()


# CREATE A NEW REWARD
def create_reward(session, rewardName, description, amount):
    new_reward = Reward(reward_name=rewardName, description=description, amount=amount)
    session.add(new_reward)
    print('new reward added: {}'.format(rewardName))
    session.commit()

# CREATE A NEW PUNISHMENT
def create_punishment(session, punishmentName, description, amount):
    new_punishment = Punishment(punishment_name=punishmentName, description=description, amount=amount)
    session.add(new_punishment)
    print('new punishment added: {}'.format(punishmentName))
    session.commit()

