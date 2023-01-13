# Initialize the database with default data.
# Pull in the create functions from ./Functions/createFunctions.py
# create users_init function to create all users
# create chores_init function to create all chores
# create rewards_init function to create all rewards
# create punishments_init function to create all punishments
# then call those functions in the main.py to add all the data to the database

from .Functions.createFunctions import create_user, create_chore, create_reward, create_punishment

# Create all the users
def init_users(session):
    create_user(session, 'DAD', 'secret', 'dad@test.com', 'parent', 60.00)
    create_user(session, 'MOM', 'secret', 'mom@test.com', 'parent', 60.00)
    create_user(session, 'CHILD1', 'secret', 'child1@test.com', 'child', 0.00)
    create_user(session, 'CHILD2', 'secret', 'child2@test.com', 'child', 0.00)
    create_user(session, 'CHILD3', 'secret', 'child3@test.com', 'child', 0.00)

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

def init_data(session):
    # initialize all users
    init_users(session)

    # initialize all chores
    init_chores(session)

    # initialize all rewards
    init_rewards(session)

    # initialize all punishments
    init_punishments(session)

    # close the db session
    session.close()
