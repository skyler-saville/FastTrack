# dbConnection.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .dbInit import init_data

from dotenv import load_dotenv
load_dotenv()

_DB_URL = os.getenv('DATABASE_URL')

from .models import Base

def create_db_engine():
    # Replace 'DATABASE_URI' with the actual database URI
    engine = create_engine(_DB_URL)
    # check if database is connected
    try:
        conn = engine.connect()
        print("App connected to database successfully")
        # drop all tables before creating all tables
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        conn.close()
        return engine
    except Exception as e:
        print("Error: Connecting App to database failed")
        print(e)


def get_db_session(engine):
    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = Session()
    return session

_DB_ENGINE = create_db_engine()

# call the init_data function 
# to initialize the database 
# with all the users, chores, rewards and punishments
init_data(get_db_session(_DB_ENGINE))
