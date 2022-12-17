import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv
load_dotenv()

_DB_URL = os.getenv('DATABASE_URL')

from .models import Base

def create_db_engine():
    # Replace 'DATABASE_URI' with the actual database URI
    engine = create_engine(_DB_URL)
    Base.metadata.create_all(engine)
    return engine

def get_db_session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

_DB_ENGINE = create_db_engine()
