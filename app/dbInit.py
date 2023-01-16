# Initialize the database with default data.
# Pull in the create functions from ./Functions/createFunctions.py
# create users_init function to create all users
# create chores_init function to create all chores
# create rewards_init function to create all rewards
# create punishments_init function to create all punishments
# then call those functions in the main.py to add all the data to the database

from .Functions.createFunctions import create_user, create_chore, create_reward, create_punishment
# use for testing database functionality 
from .Functions.readFunctions import read_user, read_users, read_chore, read_chores, read_reward, read_rewards, read_punishment, read_punishments
from .Functions.updateFunctions import update_user, update_chore, update_reward, update_punishment
from .Functions.deleteFunctions import delete_user, delete_chore, delete_reward, delete_punishment

# Create all the users
def init_users(session, userData):
    for user in userData:
        try:
            result = create_user(session, user['username'], user['password'], user['email'], user['userRole'], user['balance'])
            if result.success is False:
                raise Exception(result.message)
        except Exception as e:
            print(e)


def init_chores(session):
    create_chore(session, 'Clean and Vacuum Bedroom', 'Clean the entire bedroom and then vacuum.', 2.00)
    create_chore(session, 'Clean Shower or Tub', 'Wipe down the entire shower or bathtub.', 2.00)
    create_chore(session, 'Clean Toilet', 'Wipe down toilet with Clorox wipe, then use cleaner and brush to clean the bowl. Make sure to wipe the floor around the toilet too (each).', 2.00)
    create_chore(session, 'Sink and Mirror', 'Clean the sink and counter, then wipe down the mirror (each).', 2.00)
    create_chore(session, 'Sweep and Mop', 'Sweep and mop all the wood floor.', 2.00)
    create_chore(session, 'Wash Dishes', 'Wash dishes and load/start dishwasher.', 2.00)
    create_chore(session, 'Mop Baseboards', 'Clean all the baseboards.', 1.00)
    create_chore(session, 'Set Table', 'Set out plates, cups, forks, knives, spoons (whatever is needed for the meal).', 1.00)
    create_chore(session, 'Dust', 'Dust all the main parts of the house (non-bedroom rooms).', 1.00)
    create_chore(session, 'Empty Garbages', 'Empty garbage and recycle bins into dumpsters outside.', 1.00)
    create_chore(session, 'Clear of Table', 'Clear kitchen table and wipe it down.', 1.00)
    create_chore(session, 'Scoop Poop', 'Clean up poop in both front and back yards.', 1.00)
    create_chore(session, 'Laundry', 'Fold and put away laundry.', 0.50)
    create_chore(session, 'Pick-up Toys', 'Clean all toys located outside of room.', 0.50)
    create_chore(session, 'Dirty Clothes', 'Put dirty clothes in the hamper.', 0.50)
    create_chore(session, 'Feed Puppies', 'Feed both Lola and Kozmo.', 0.50)
    create_chore(session, 'Take Puppy out', 'Take out Lola or Kozmo.', 0.50)
    create_chore(session, 'Empty Dishwasher', 'Empty a section of the dishwasher.', 0.50)

def init_rewards(session):
    create_reward(session, 'Xbox Time', 'In-fighting with sibling(s)', -2.00)
    create_reward(session, 'Dollar Store Trip', 'Purchase 1 item at the dollar store', -1.00)
    create_reward(session, '$10 Cash', 'Convert your in-app balance to IRL cash', -10.00)
    create_reward(session, 'Movie Night', 'You pick a movie and the candy', -5.00)
    create_reward(session, 'Fiesta Fun', 'Take a trip to ride go-carts or whatever you want', -20.00)
    create_reward(session, 'Clothes Shopping', 'Get a new item of clothing (online or in a store)', -15.00)
    create_reward(session, '$10 Giftcard', 'Get a $10 Giftcard to somewhere', -10.00)
    create_reward(session, 'Video Game', 'Buy a new video game', -40.00)
    create_reward(session, 'Date with Parent(s)', 'Take Mom and/or Dad to a place of your choosing', -25.00)
    create_reward(session, 'Ice Cream Party', 'Ice Cream, Toppings and Friends', -30.00)

def init_punishments(session):
    create_punishment(session, 'Fighting', 'In-fighting with sibling(s)', -2.00)
    create_punishment(session, 'Talking Back', 'Talking back to parent after being told to do something.', -4.00)
    create_punishment(session, 'Not Listening', 'Not listening after being told several times', -2.00)
    create_punishment(session, 'Bad Attitude', 'Having an overall negative attitude about what is being done', -4.00)
    create_punishment(session, 'Saying Shut-up', 'Telling a parent or sibling to "shut-up"', -10.00)
    create_punishment(session, 'Yelling', 'Yelling at a sibling', -10.00)
    create_punishment(session, 'Bossing', 'Bossing around sibling(s)', -4.00)
    create_punishment(session, 'Negative Comments', 'Adding negative comments to any situation', -4.00)
    create_punishment(session, 'Blaming', 'Blaming someone else and not owning your mistakes', -2.00)
    create_punishment(session, 'Whining', 'Whining when you are not getting what you want', -2.00)

def inti_tests(session):
    # create a group of users that should fail
    create_user(session, 'Email Test', 'password', 'email@test', 'parent', 60.00)  # invalid email test
    create_user(session, 'Role Test', 'secret', 'role@test.com', 'admin', 100.00)    # invalid user role test
    create_user(session, 'Positive Balance Test', 'secret', 'highbalance@test.com', 'child', 1000.00) # high balance test
    create_user(session, 'Negative Balance Test', 'secret', 'lowbalance@test.com', 'child', -1000.00) # high balance test
    create_user(session, 'Superlong Username Test to see if it will throw and error upon created', 'secret', 'logname@test.com', 'parent', 60.00) # long username test
    create_user(session, 'Duplicate Dad', 'password', 'dad@test.com', 'parent', 43.00)  # duplicated user test

    # create a group of users that will be modified later
    create_user(session, 'Mr. Red', 'secret', 'misterBlack@test.com', 'parent', 50.00)  # username will be changed to mister black later
    create_user(session, 'forgetful', 'i dont know', 'forgetPass@test.com', 'child', 0.00) # password update test
    create_user(session, 'change me', 'change me', 'change@me.com', 'parent', 20),  # change every field test
    create_user(session, 'delete me', 'blah', 'delete@me.com', 'child', 20.00)

    # create some test chores
    create_chore(session, 'oink', 'put pigs in the field', 6000.00) # too high amount test
    create_chore(session, 'bah', 'put the sheep in the woods', -60.00) # too low amount test
    create_chore(session, 'oink', 'why are you oinking at me again?', 10.00) #duplicate choreName 
    # create some test rewards
    create_reward(session, 'ZOO VISIT', 'go to the zoo... stay at the zoo', 75.00) # positive amount test
    create_reward(session, 'guns', 'Go sHoOt GUnS at ThE GUn rAnge', -75.00) # string format test
    # create some test punishments
    create_punishment(session, 'GrounDeD', "you're grounded... Stay in YouR rOOm!", -111.00) # string format test
    create_punishment(session, 'scrape gum', 'scrape gum off the street', 10.00) # pretend chore as punishment
    create_punishment(session, 'bossing around siblings', 'this chore is technically a dublicate', -10.00) # duplicate test -- will pass until validation is added
    create_punishment(session, 'You are broke', 'low amount of money test', -10000) # low amount test

    # Update the test users
    update_user(session, 'who?', 'Ghost user', 'iStillDont@know.who', 'child', 'thispasswordsucks')
    
defaultUserData = [
    {'username':'DAD', 'password':'secret', 'email':'dad@test.com', 'userRole':'parent', 'balance': 60.00},
    {'username':'MOM', 'password':'secret', 'email':'mom@test.com', 'userRole':'parent', 'balance': 60.00},
    {'username':'CHILD1', 'password':'secret', 'email':'child1@test.com', 'userRole':'child', 'balance': 0.00},
    {'username':'CHILD2', 'password':'secret', 'email':'child2@test.com', 'userRole':'child', 'balance': 0.00},
    {'username':'CHILD3', 'password':'secret', 'email':'child3@test.com', 'userRole':'child', 'balance': 0.00}
]   

testUserData = [
    {'username':'Email Test', 'password':'password', 'email':'email@test', 'userRole':'parent', 'balance': 60.00},      # invalid email test
    {'username':'Role Test', 'password':'secret', 'email':'role@test.com', 'userRole':'admin', 'balance': 100.00},      # invalid user role test
    {'username':'Positive Balance Test', 'password':'secret', 'email':'highbalance@test.com', 'userRole':'child', 'balance': 1000.00},
    {'username':'Negative Balance Test', 'password':'secret', 'email':'lowbalance@test.com', 'userRole':'child', 'balance': -1000.00},
    {'username':'Superlong Username Test to see if it will throw and error upon created', 'password':'secret', 'email':'logname@test.com', 'userRole':'parent', 'balance': 60.00},  # long username test
    {'username':'Duplicate Dad', 'password':'secret', 'email':'dad@test.com', 'userRole':'parent', 'balance': 43.00},   # duplicated user test
]   

modifyUsersData = [
    {'username':'Mr. Red', 'password':'secret', 'email':'misterBlack@test.com', 'userRole':'parent', 'balance': 50.00},  # username will be changed to mister black later
    {'username':'forgetful', 'password':'i dont know', 'email':'forgetPass@test.com', 'userRole':'child', 'balance': 0.00}, # password update test
    {'username':'change me', 'password':'notata', 'email':'nota@float.com', 'userRole':'parent', 'balance': 20},  # change every field test ... not float
    {'username':'delete me', 'password':'blah', 'email':'delete@me.com', 'userRole':'child', 'balance': 20.00}
]

def init_data(session):
    # initialize all users
    init_users(session, defaultUserData)


    # initialize all chores
    init_chores(session)

    # initialize all rewards
    init_rewards(session)

    # initialize all punishments
    init_punishments(session)

    # init tests
    # inti_tests(session)
    init_users(session, modifyUsersData)
    init_users(session, testUserData)

    # close the db session
    session.close()
