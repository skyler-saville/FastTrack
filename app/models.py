# models.py
from sqlalchemy import Column, String, DateTime, Enum, Integer, Numeric, Table, ForeignKeyConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()

# user_parents association table
# Define association table for many-to-many relationship between parents and children
user_parents = Table('user_parents', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.user_id'), primary_key=True),
    Column('parent_id', Integer, ForeignKey('users.user_id'), primary_key=True)
)

# Users Model
class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    created_on = Column(DateTime, nullable=False)
    last_login = Column(DateTime)
    user_role = Column(Enum('child', 'parent', name='roles')) # might add 'organizer' & 'admin' roles later
    balance = Column(Numeric(5, 2))
    # Added parents relationship to query parent-child relationships
    parents = relationship("User", secondary=user_parents, primaryjoin=user_id==user_parents.c.user_id,
    secondaryjoin=user_id==user_parents.c.parent_id)

# Chores Model
class Chore(Base):
    __tablename__ = 'chores'

    chore_id = Column(Integer, primary_key=True)
    chore_name = Column(String(50), nullable=False)
    description = Column(String(150))
    amount = Column(Numeric(5, 2))
    created_on = Column(DateTime, nullable=False)
    edited_on = Column(DateTime)

# Rewards Model
class Reward(Base):
    __tablename__ = 'rewards'

    reward_id = Column(Integer, primary_key=True)
    reward_name = Column(String(50), nullable=False)
    description = Column(String)
    amount = Column(Numeric(5, 2))
    created_on = Column(DateTime, nullable=False)
    edited_on = Column(DateTime)

# Punishments Model
class Punishment(Base):
    __tablename__ = 'punishments'

    punishment_id = Column(Integer, primary_key=True)
    punishment_name = Column(String(50), nullable=False)
    description = Column(String)
    amount = Column(Numeric(5, 2))
    created_on = Column(DateTime, nullable=False)
    edited_on = Column(DateTime)

# user_chores association table
# Define association table for many-to-many relationship between users and chores
user_chores = Table('user_chores', Base.metadata,
    Column('chore_id', Integer, primary_key=True),
    Column('user_id', Integer, primary_key=True),
    Column('chore_status', Enum('assigned', 'completed', name='chore_status'), nullable=False, default='assigned'),
    Column('completed_on', DateTime),
    ForeignKeyConstraint(['chore_id'], ['chores.chore_id'], ondelete='CASCADE'),
    ForeignKeyConstraint(['user_id'], ['users.user_id'], ondelete='CASCADE')
)


# user_rewards association table
# Define association table for many-to-many relationship between users and rewards
user_rewards = Table('user_rewards', Base.metadata,
    Column('reward_id', Integer, primary_key=True),
    Column('user_id', Integer, primary_key=True),
    Column('completed_on', DateTime, nullable=False, default='CURRENT_TIMESTAMP'),
    ForeignKeyConstraint(['reward_id'], ['rewards.reward_id'], ondelete='CASCADE'),
    ForeignKeyConstraint(['user_id'], ['users.user_id'], ondelete='CASCADE')
)

# user_punishments association table
# Define association table for many-to-many relationship between users and punishments
user_punishments = Table('user_punishments', Base.metadata,
    Column('punishment_id', Integer, primary_key=True),
    Column('user_id', Integer, primary_key=True),
    Column('completed_on', DateTime, nullable=False, default='CURRENT_TIMESTAMP'),
    ForeignKeyConstraint(['punishment_id'], ['punishments.punishment_id'], ondelete='CASCADE'),
    ForeignKeyConstraint(['user_id'], ['users.user_id'], ondelete='CASCADE')
)


