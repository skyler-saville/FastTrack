from sqlalchemy import Table, Column, DateTime, ForeignKey, PrimaryKeyConstraint, Integer, String, Numeric, Enum, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID, VARCHAR, TIMESTAMP

from users import User

Base = declarative_base()


user_chores = Table(
    "user_chores",
    Base.metadata,
    Column("user_id", ForeignKey("users.user_id"), primary_key=True),
    Column("chore_id", ForeignKey("chores.chore_id"), primary_key=True)

)


class Chores(Base):
    __tablename__ = "chores"

    chore_id = Column(Integer, primary_key=True)
    chore_name = Column(String(50).with_variant(VARCHAR(50, charset="utf8"), "postgres"), unique=True, nullable=False)
    description = Column(Text)
    amount = Column(Numeric(10, 2))





