CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- users table
CREATE TABLE IF NOT EXISTS users (    
    user_id uuid DEFAULT uuid_generate_v4 (),
    username VARCHAR ( 50 ) NOT NULL,
    password VARCHAR ( 50 ) NOT NULL,
    email VARCHAR ( 255 ) UNIQUE NOT NULL,
    created_on TIMESTAMP NOT NULL,
    last_login TIMESTAMP,
    bank_total MONEY,
    PRIMARY KEY (user_id)
);

-- chores table
CREATE TABLE IF NOT EXISTS chores (
    chore_id uuid DEFAULT uuid_generate_v4 (),
    chore_name VARCHAR ( 50 ) NOT NULL,
    description TEXT,
    amount MONEY,
    PRIMARY KEY (chore_id)
);

-- rewards table (withdraws from users bank_total)
CREATE TABLE IF NOT EXISTS rewards (
    reward_id uuid DEFAULT uuid_generate_v4 (),
    reward_name VARCHAR ( 50 ) NOT NULL,
    description TEXT,
    amount MONEY,
    PRIMARY KEY (reward_id)
);

-- punishments table (withdraws from users bank_total)
CREATE TABLE IF NOT EXISTS punishments (
    punishment_id uuid DEFAULT uuid_generate_v4 (),
    punishment_name VARCHAR ( 50 ) NOT NULL,
    description TEXT,
    amount MONEY,
    PRIMARY KEY (punishment_id)
);



--  initalize parents (with $60 each available)
INSERT INTO users(username, password, email, created_on, bank_total)
VALUES('father', 'secret', 'father@test.com', CURRENT_TIMESTAMP, '$60.00');

INSERT INTO users(username, password, email, created_on, bank_total)
VALUES('mother', 'secret', 'mother@test.com', CURRENT_TIMESTAMP, '$60.00');

-- initalize children (with no money available)
INSERT INTO users(username, password, email, created_on, bank_total)
VALUES('daughter', 'secret', 'daughter@test.com', CURRENT_TIMESTAMP, '$0.00');

INSERT INTO users(username, password, email, created_on, bank_total)
VALUES('son1', 'secret', 'son1@test.com', CURRENT_TIMESTAMP, '$0.00');

INSERT INTO users(username, password, email, created_on, bank_total)
VALUES('son2', 'secret', 'son2@test.com', CURRENT_TIMESTAMP, '$0.00');
-- insert all the chores into the chores table

INSERT INTO chores(chore_name, description, amount)
VALUES('Clean Shower or Tub', 'Wipe down the entire shower or bathtub.', '$2.00');

INSERT INTO chores(chore_name, description, amount)
VALUES('Clean and Vacuum Bedroom', 'Clean the entire bedroom and then vacuum. ', '$2.00');

INSERT INTO chores(chore_name, description, amount)
VALUES('Clean Toilet', 'Wipe down toilet with Clorox wipe, then use cleaner and brush to clean the bowl. Make sure to wipe the floor around the toilet too (each).', '$2.00');

INSERT INTO chores(chore_name, description, amount)
VALUES('Sink and Mirror', 'Clean the sink and counter, then wipe down the mirror (each).', '$2.00');

INSERT INTO chores(chore_name, description, amount)
VALUES('Sweep and Mop', 'Sweep and mop all the wood floor.', '$2.00');

INSERT INTO chores(chore_name, description, amount)
VALUES('Wash Dishes', 'Wash dishes and load/start dishwasher.', '$2.00');

INSERT INTO chores(chore_name, description, amount)
VALUES('Mop Baseboards', 'Clean all the baseboards.', '$1.00');

INSERT INTO chores(chore_name, description, amount)
VALUES('Set Table', 'Set out plates, cups, forks, knives, spoons (whatever is needed for the meal).', '$1.00');

INSERT INTO chores(chore_name, description, amount)
VALUES('Dust', 'Dust all the main parts of the house (non-bedroom rooms).', '$1.00');

INSERT INTO chores(chore_name, description, amount)
VALUES('Empty Garbages', 'Empty garbage and recycle bins into dumpsters outside.', '$1.00');

INSERT INTO chores(chore_name, description, amount)
VALUES('Clear of Table', 'Clear kitchen table and wipe it down.', '$1.00');

INSERT INTO chores(chore_name, description, amount)
VALUES('Scoop Poop', 'Clean up poop in both front and back yards.', '$1.00');

INSERT INTO chores(chore_name, description, amount)
VALUES('Laundry', 'Fold and put away laundry.', '$0.50');

INSERT INTO chores(chore_name, description, amount)
VALUES('Pick-up Toys', 'Clean all toys located outside of room.', '$0.50');

INSERT INTO chores(chore_name, description, amount)
VALUES('Dirty Clothes', 'Put dirty clothes in the hamper.', '$0.50');

INSERT INTO chores(chore_name, description, amount)
VALUES('Feed Puppies', 'Feed both Lola and Kozmo.', '$0.50');

INSERT INTO chores(chore_name, description, amount)
VALUES('Take Puppy out', 'Take out Lola or Kozmo.', '$0.50');

INSERT INTO chores(chore_name, description, amount)
VALUES('Empty Dishwasher', 'Empty a section of the dishwasher.', '$0.50');

-- insert punishment rows into punishments table (negative dollar amounts)
INSERT INTO punishments(punishment_name, description, amount)
VALUES('Fighting', 'In-fighting with sibling(s)', '-$2.00');

INSERT INTO punishments(punishment_name, description, amount)
VALUES('Talking Back', 'Talking back to parent after being told to do something.', '-$4.00');

INSERT INTO punishments(punishment_name, description, amount)
VALUES('Not Listening', 'Not listening after being told several times', '-$2.00');

INSERT INTO punishments(punishment_name, description, amount)
VALUES('Bad Attitude', 'Having an overall negative attitude about what is being done', '-$4.00');

INSERT INTO punishments(punishment_name, description, amount)
VALUES('Saying Shut-up', 'Telling a parent or sibling to "shut-up"', '-$10.00');

INSERT INTO punishments(punishment_name, description, amount)
VALUES('Yelling', 'Yelling at a sibling', '-$10.00');

INSERT INTO punishments(punishment_name, description, amount)
VALUES('Bossing', 'Bossing around sibling(s)', '-$4.00');

INSERT INTO punishments(punishment_name, description, amount)
VALUES('Negative Comments', 'Adding negative comments to any situation', '-$4.00');

INSERT INTO punishments(punishment_name, description, amount)
VALUES('Blaming', 'Blaming someone else and not owning your mistakes', '-$2.00');

INSERT INTO punishments(punishment_name, description, amount)
VALUES('Whining', 'Whining when you are not getting what you want', '-$2.00');