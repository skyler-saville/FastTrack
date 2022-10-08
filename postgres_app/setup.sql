DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS chores;
DROP TABLE IF EXISTS rewards;
DROP TABLE IF EXISTS punishments;
DROP TABLE IF EXISTS bank;


CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TYPE ROLES as ENUM ('child', 'parent');

-- users table
CREATE TABLE IF NOT EXISTS users (    
    user_id uuid DEFAULT uuid_generate_v4 (),
    username VARCHAR ( 50 ) NOT NULL,
    password VARCHAR ( 50 ) NOT NULL,
    email VARCHAR ( 255 ) UNIQUE NOT NULL,
    created_on TIMESTAMP NOT NULL,
    last_login TIMESTAMP,
    user_role ROLES,
    bank_id uuid,
    PRIMARY KEY (user_id)
);

-- chores table
CREATE TABLE IF NOT EXISTS chores (
    chore_id uuid DEFAULT uuid_generate_v4 (),
    chore_name VARCHAR ( 50 ) NOT NULL,
    description TEXT,
    amount NUMERIC(10,2),
    PRIMARY KEY (chore_id)
);

-- rewards table (withdraws from users bank_total)
CREATE TABLE IF NOT EXISTS rewards (
    reward_id uuid DEFAULT uuid_generate_v4 (),
    reward_name VARCHAR ( 50 ) NOT NULL,
    description TEXT,
    amount NUMERIC(10,2),
    PRIMARY KEY (reward_id)
);

-- punishments table (withdraws from users bank_total)
CREATE TABLE IF NOT EXISTS punishments (
    punishment_id uuid DEFAULT uuid_generate_v4 (),
    punishment_name VARCHAR ( 50 ) NOT NULL,
    description TEXT,
    amount NUMERIC(10,2),
    PRIMARY KEY (punishment_id)
);

CREATE TABLE IF NOT EXISTS bank (
    bank_id uuid DEFAULT uuid_generate_v4 (),
    user_id uuid,
    balance NUMERIC(10,2) DEFAULT 0.00,
    PRIMARY KEY (bank_id),
    CONSTRAINT fk_user
        FOREIGN KEY (user_id)   
            REFERENCES users(user_id)
);

--  initalize parents (with $60 each available)
INSERT INTO users(username, password, email, created_on, user_role)
    VALUES('dad', 'secret', 'dad@test.com', CURRENT_TIMESTAMP, 'parent'),
    ('mom', 'secret', 'mom@test.com', CURRENT_TIMESTAMP, 'parent'),
    ('child1', 'secret', 'child1@test.com', CURRENT_TIMESTAMP, 'child'),
    ('child2', 'secret', 'child2@test.com', CURRENT_TIMESTAMP, 'child'),
    ('child3', 'secret', 'child3@test.com', CURRENT_TIMESTAMP, 'child');
-- insert all the chores into the chores table

-- TODO: automatically assign a bank account to each user upon creating user
INSERT INTO bank (user_id)
    SELECT user_id FROM users;

INSERT INTO chores(chore_name, description, amount)
    VALUES('Clean Shower or Tub', 'Wipe down the entire shower or bathtub.', 2.00),
    ('Clean and Vacuum Bedroom', 'Clean the entire bedroom and then vacuum. ', 2.00),
    ('Clean Toilet', 'Wipe down toilet with Clorox wipe, then use cleaner and brush to clean the bowl. Make sure to wipe the floor around the toilet too (each).', 2.00),
    ('Sink and Mirror', 'Clean the sink and counter, then wipe down the mirror (each).', 2.00),
    ('Sweep and Mop', 'Sweep and mop all the wood floor.', 2.00),
    ('Wash Dishes', 'Wash dishes and load/start dishwasher.', 2.00),
    ('Mop Baseboards', 'Clean all the baseboards.', 1.00),
    ('Set Table', 'Set out plates, cups, forks, knives, spoons (whatever is needed for the meal).', 1.00),
    ('Dust', 'Dust all the main parts of the house (non-bedroom rooms).', 1.00),
    ('Empty Garbages', 'Empty garbage and recycle bins into dumpsters outside.', 1.00),
    ('Clear of Table', 'Clear kitchen table and wipe it down.', 1.00),
    ('Scoop Poop', 'Clean up poop in both front and back yards.', 1.00),
    ('Laundry', 'Fold and put away laundry.', 0.50),
    ('Pick-up Toys', 'Clean all toys located outside of room.', 0.50),
    ('Dirty Clothes', 'Put dirty clothes in the hamper.', 0.50),
    ('Feed Puppies', 'Feed both Lola and Kozmo.', 0.50),
    ('Take Puppy out', 'Take out Lola or Kozmo.', 0.50),
    ('Empty Dishwasher', 'Empty a section of the dishwasher.', 0.50);

-- insert punishment rows into punishments table (negative dollar amounts)
INSERT INTO punishments(punishment_name, description, amount)
    VALUES('Fighting', 'In-fighting with sibling(s)', -2.00),
    ('Talking Back', 'Talking back to parent after being told to do something.', -4.00),
    ('Not Listening', 'Not listening after being told several times', -2.00),
    ('Bad Attitude', 'Having an overall negative attitude about what is being done', -4.00),
    ('Saying Shut-up', 'Telling a parent or sibling to "shut-up"', -10.00),
    ('Yelling', 'Yelling at a sibling', -10.00),
    ('Bossing', 'Bossing around sibling(s)', -4.00),
    ('Negative Comments', 'Adding negative comments to any situation', -4.00),
    ('Blaming', 'Blaming someone else and not owning your mistakes', -2.00),
    ('Whining', 'Whining when you are not getting what you want', -2.00);