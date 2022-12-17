# models.py
from sqlalchemy import Column, String, DateTime, Enum, Integer, Numeric, Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Users Model
class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    created_on = Column(DateTime, nullable=False)
    last_login = Column(DateTime)
    user_role = Column(Enum('child', 'parent', name='roles'))
    balance = Column(Numeric(10, 2))

# Chores Model
class Chore(Base):
    __tablename__ = 'chores'

    chore_id = Column(Integer, primary_key=True)
    chore_name = Column(String(50), nullable=False)
    description = Column(String)
    amount = Column(Numeric(10, 2))

# Rewards Model
class Reward(Base):
    __tablename__ = 'rewards'

    reward_id = Column(Integer, primary_key=True)
    reward_name = Column(String(50), nullable=False)
    description = Column(String)
    amount = Column(Numeric(10, 2))

# Punishments Model
class Punishment(Base):
    __tablename__ = 'punishments'

    punishment_id = Column(Integer, primary_key=True)
    punishment_name = Column(String(50), nullable=False)
    description = Column(String)
    amount = Column(Numeric(10, 2))

# user_chores association table
# Define association table for many-to-many relationship between users and chores
user_chores = Table('user_chores', Base.metadata,
    Column('chore_id', Integer, primary_key=True),
    Column('user_id', Integer, primary_key=True),
    Column('chore_status', Enum('assigned', 'completed', name='chore_status'), nullable=False, default='assigned'),
    Column('completed_on', DateTime)
)


# user_rewards association table
# Define association table for many-to-many relationship between users and rewards
user_rewards = Table('user_rewards', Base.metadata,
    Column('reward_id', Integer, primary_key=True),
    Column('user_id', Integer, primary_key=True),
    Column('completed_on', DateTime, nullable=False, default='CURRENT_TIMESTAMP')
)

# user_punishments association table
# Define association table for many-to-many relationship between users and punishments
user_punishments = Table('user_punishments', Base.metadata,
    Column('punishment_id', Integer, primary_key=True),
    Column('user_id', Integer, primary_key=True),
    Column('completed_on', DateTime, nullable=False, default='CURRENT_TIMESTAMP')
)