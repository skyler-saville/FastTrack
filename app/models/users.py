from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID, VARCHAR, TIMESTAMP, MONEY
from uuid import uuid4

Base = declarative_base()

#    user_id uuid DEFAULT uuid_generate_v4 (),
#    username VARCHAR ( 50 ) NOT NULL,
#    password VARCHAR ( 50 ) NOT NULL,
#    email VARCHAR ( 255 ) UNIQUE NOT NULL,
#    created_on TIMESTAMP NOT NULL,
#    last_login TIMESTAMP,
#    bank_total MONEY,
#    PRIMARY KEY (user_id)


# TODO change the user bank_total to be the foreign key to a bank id

class User(Base):
    __tablename__ = "users"
    USER_ID = Column("user_id", UUID(as_uuid=True), primary_key=True, default=uuid4)
    USERNAME = Column("username", String(50).with_variant(VARCHAR(50, charset="utf8"), "postgres"), unique=True, nullable=False)
    PASSWORD = Column("password", String(50).with_variant(VARCHAR(50, charset="utf8"), "postgres"), nullable=False)
    EMAIL = Column("email", String(255).with_variant(VARCHAR(255, charset="utf8"), "postgres"), nullable=False, unique=True)
    CREATED_ON = Column("created_on", TIMESTAMP(timezone=False), nullable=False, oncreated=func.now())
    LAST_LOGIN = Column("last_login", TIMESTAMP(timezone=False), nullable=True, onlogin=func.now())
    BANK_TOTAL = Column("bank_total", Numeric(10,2), ForeignKey("bank.bank_id"),nullable=True)

    bank = relationship('Bank')

class Bank(Base):
    __tablename__ = "bank"
    BANK_ID = Column("user_id", UUID(as_uuid=True), primary_key=True, default=uuid4)
    BALANCE = Column("balance", Numeric(10,2))