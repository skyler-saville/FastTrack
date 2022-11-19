from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Numeric, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID, VARCHAR, TIMESTAMP
# from uuid import uuid4

Base = declarative_base()

#    user_id uuid DEFAULT uuid_generate_v4 (),  <-- change SERIAL to UUID after everything is connected and working?

#       __tablename__ = "users"
#       user_id SERIAL PRIMARY KEY
#       username VARCHAR ( 50 ) NOT NULL,
#       password VARCHAR ( 50 ) NOT NULL,
#       email VARCHAR ( 255 ) UNIQUE NOT NULL,
#       created_on TIMESTAMP NOT NULL,
#       last_login TIMESTAMP,
#       user_roles ENUM('child', 'parent')
#       balance NUMERIC(10,2)

class User(Base):
    __tablename__ = "users"

    # USER_ID = Column("user_id", UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(Integer, primary_key=True)
    username = Column(String(50).with_variant(VARCHAR(50, charset="utf8"), "postgres"), unique=True, nullable=False)
    password = Column(String(50).with_variant(VARCHAR(50, charset="utf8"), "postgres"), nullable=False)
    email = Column(String(255).with_variant(VARCHAR(255, charset="utf8"), "postgres"), nullable=False, unique=True)
    created_on = Column(TIMESTAMP(timezone=False), nullable=False, oncreated=func.now())
    last_login = Column(TIMESTAMP(timezone=False), nullable=True, onlogin=func.now())
    user_roles = Column(Enum('child', 'parent', name='ROLES'))
    balance = Column(Numeric(10,2))
