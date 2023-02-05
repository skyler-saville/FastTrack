"""
Use this test file to test the User CRUD operations
- Start with create_user
"""
import pytest
from .createFunctions import create_user
from .errorHandlerFunctions import UserInputError
from ..dbConnection import get_db_session, _DB_ENGINE
from ..models import User


def test_create_user():
    if __name__ == '__main__':
        print('testing create user')
        testUsers = [
            {'username':'Email Test', 'password':'P@ssword1', 'email':'email@test', 'userRole':'parent', 'balance': 60.00},      # invalid email test
            {'username':'Role Test', 'password':'P@ssword1', 'email':'role@test.com', 'userRole':'admin', 'balance': 100.00},      # invalid user role test
            {'username':'Positive Balance Test', 'password':'P@ssword1', 'email':'highbalance@test.com', 'userRole':'child', 'balance': 1000.00},
            {'username':'Negative Balance Test', 'password':'P@ssword1', 'email':'lowbalance@test.com', 'userRole':'child', 'balance': -1000.00},
            {'username':'Superlong Username Test to see if it will throw and error upon created', 'password':'P@ssword1', 'email':'logname@test.com', 'userRole':'parent', 'balance': 60.00},  # long username test
            {'username':'Duplicate Dad', 'password':'P@ssword1', 'email':'dad@test.com', 'userRole':'parent', 'balance': 43.00},   # duplicated user test
            # modify user data
            {'username':'Mr. Red', 'password':'P@ssword1', 'email':'misterBlack@test.com', 'userRole':'parent', 'balance': 50.00},  # username will be changed to mister black later
            {'username':'forgetful', 'password':'P@ssword1', 'email':'forgetPass@test.com', 'userRole':'child', 'balance': 0.00}, # password update test
            {'username':'change me', 'password':'P@ssword1', 'email':'nota@float.com', 'userRole':'parent', 'balance': 20},  # change every field test ... not float
            {'username':'delete me', 'password':'P@ssword1', 'email':'delete@me.com', 'userRole':'child', 'balance': 20.00},
            # additional users
            {'username':'testuser1', 'password':'P@ssword1', 'email':'testuser1@example.com', 'userRole':'parent', 'balance': 50.00},    
            {'username':'testuser2', 'password':'P@ssword1', 'email':'testuser2@example.com', 'userRole':'parent', 'balance': 50.00},    
            {'username':'testuser4', 'password':'P@ssword1', 'email':'testuser4@example.com', 'userRole':'child', 'balance': 10.00},    
            {'username':'testuser3', 'password':'P@ssword1', 'email':'testuser3@example.com', 'userRole':'child', 'balance': 0.00},    
            {'username':'testuser5', 'password':'password', 'email':'testuser5@example.com', 'userRole':'child', 'balance': -10.00},    
            {'username':'testuser6', 'password':'P@ssword1', 'email':'testuser6@example.com', 'userRole':'child', 'balance': 10.00},    
            {'username':'testuser7', 'password':'P@ssword1', 'email':'', 'userRole':'child', 'balance': 10.00},    
            {'username':'testuser8', 'password':'P@ssword1', 'email':'testuser8@example.com', 'userRole':'', 'balance': 10.00},    
            {'username':'', 'password':'P@ssword1', 'email':'testuser9@example.com', 'userRole':'child', 'balance': 10.00},    
            {'username':'testuser10', 'password':'P@ssword1', 'email':'testuser10@example.com', 'userRole':'child', 'balance': 10.00},    
            {'username':'testuser10', 'password':'P@ssword1', 'email':'testuser11@example.com', 'userRole':'child', 'balance': 10.00},
            {'username':'john_doe', 'password':'P@ssword1', 'email':'johndoe@example.com', 'userRole':'parent', 'balance': 60.00},
            {'username':'jane_doe', 'password':'P@ssword1', 'email':'janedoe@example.com', 'userRole':'parent', 'balance': 70.00},
            {'username':'jim_smith', 'password':'P@ssword1', 'email':'jimsmith@example.com', 'userRole':'parent', 'balance': 80.00},
            {'username':'sarah_lee', 'password':'P@ssword1', 'email':'sarahlee@example.com', 'userRole':'parent', 'balance': 90.00},
            {'username':'mike_brown', 'password':'P@ssword1', 'email':'mikebrown@example.com', 'userRole':'parent', 'balance': 100.00},
            {'username':'emma_watson', 'password':'P@ssword1', 'email':'emmawatson@example.com', 'userRole':'parent', 'balance': 110.00},
            {'username':'chris_evans', 'password':'P@ssword1', 'email':'chrisevans@example.com', 'userRole':'parent', 'balance': 120.00},
            {'username':'jennifer_lawrence', 'password':'P@ssword1', 'email':'jenniferlawrence@example.com', 'userRole':'parent', 'balance': 130.00},
            {'username':'brad_pitt', 'password':'P@ssword1', 'email':'bradpitt@example.com', 'userRole':'parent', 'balance': 140.00},
            {'username':'shakira', 'password':'P@ssword1', 'email':'shakira@example.com', 'userRole':'parent', 'balance': 150.00},
            {'username':'michael_jackson', 'password':'P@ssword1', 'email':'michaeljackson@example.com', 'userRole':'parent', 'balance': 160.00},
            {'username':'madonna', 'password':'P@ssword1', 'email':'madonna@example.com', 'userRole':'parent', 'balance': 170.00},
            {'username': 'nelson', 'password': 'P@ssword1', 'email': 'nelson@email.com', 'userRole': 'child', 'balance': 50.0},
            {'username': 'oprah', 'password': 'P@ssword1', 'email': 'oprah@email.com', 'userRole': 'parent', 'balance': 100.0},
            {'username': 'paul', 'password': 'P@ssword1', 'email': 'paul@email.com', 'userRole': 'child', 'balance': 75.0},
            {'username': 'queen', 'password': 'P@ssword1', 'email': 'queen@email.com', 'userRole': 'parent', 'balance': 150.0},
            {'username': 'roger', 'password': 'P@ssword1', 'email': 'roger@email.com', 'userRole': 'child', 'balance': 25.0},
            {'username': 'susan', 'password': 'P@ssword1', 'email': 'susan@email.com', 'userRole': 'parent', 'balance': 200.0},
            {'username': 'tom', 'password': 'P@ssword1', 'email': 'tom@email.com', 'userRole': 'child', 'balance': 50.0},
            {'username': 'ursula', 'password': 'P@ssword1', 'email': 'ursula@email.com', 'userRole': 'parent', 'balance': 100.0},
            {'username': 'victor', 'password': 'P@ssword1', 'email': 'victor@email.com', 'userRole': 'child', 'balance': 75.0},
            {'username': 'wendy', 'password': 'P@ssword1', 'email': 'wendy@email.com', 'userRole': 'parent', 'balance': 150.0},
            {'username': 'xavier', 'password': 'P@ssword1', 'email': 'xavier@email.com', 'userRole': 'child', 'balance': 25.0},
            {'username': 'yolanda', 'password': 'P@ssword1', 'email': 'yolanda@email.com', 'userRole': 'parent', 'balance': 200.0},
            {'username': 'zachary', 'password': 'P@ssword1', 'email': 'zachary@email.com', 'userRole': 'child', 'balance': 50.0}
        ]   

        session = get_db_session(_DB_ENGINE)

        for u in testUsers:
            try:
                with pytest.raises(UserInputError):
                    user = create_user(session, u['username'], u['password'], u['email'], u['userRole'], u['balance'])
                # assert that the create_user function returns a User object
                assert isinstance(user, User)
                # assert that the returned object's fields match the input data
                assert user.username == u['username']
                assert user.email == u['email']
                assert user.user_role == u['userRole']
                assert user.balance == u['balance']
                # rollback the session after creating and testing the newly added user
                print(f'rolling back {user}')
                session.rollback()
                session.flush()
            except Exception as e:
                print(e)
        # after running all test users through the test, close the session
        session.close()

    
test_create_user()