DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS chores;
DROP TABLE IF EXISTS user_chores;
DROP TABLE IF EXISTS rewards;
DROP TABLE IF EXISTS user_rewards;
DROP TABLE IF EXISTS punishments;
DROP TABLE IF EXISTS user_punishments;


-- CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TYPE ROLES as ENUM ('child', 'parent');
CREATE TYPE CHORE_STATUS as ENUM ('','assigned', 'completed');

-- users table
CREATE TABLE IF NOT EXISTS users (    
    -- user_id uuid DEFAULT uuid_generate_v4 (),
    user_id SERIAL PRIMARY KEY,
    username VARCHAR ( 50 ) NOT NULL,
    password VARCHAR ( 50 ) NOT NULL,
    email VARCHAR ( 255 ) UNIQUE NOT NULL,
    created_on TIMESTAMP NOT NULL,
    last_login TIMESTAMP,
    user_role ROLES,
    balance NUMERIC(10,2)
    -- REMOVED THE CONNECTION TO THE NON-EXISTANT BANK TABLE
);

-- chores table
CREATE TABLE IF NOT EXISTS chores (
    -- chore_id uuid DEFAULT uuid_generate_v4 (),
    chore_id SERIAL PRIMARY KEY,
    chore_name VARCHAR ( 50 ) NOT NULL,
    description TEXT,
    amount NUMERIC(10,2)
);

-- user_chores linking table
CREATE TABLE IF NOT EXISTS user_chores (
    chore_id INTEGER REFERENCES chores(chore_id),
    user_id INTEGER REFERENCES users(user_id),
    _status CHORE_STATUS NOT NULL DEFAULT '',
    completed_on TIMESTAMP,
    CONSTRAINT UC_user_chore UNIQUE (chore_id, user_id, _status, completed_on)
    -- CONSTRAINT user_chores_pkey PRIMARY KEY(chore_id, user_id)
    -- removed constraint to allow multiple entries for same user
);


-- rewards table (withdraws from users bank_total)
CREATE TABLE IF NOT EXISTS rewards (
    -- reward_id uuid DEFAULT uuid_generate_v4 (),
    reward_id SERIAL PRIMARY KEY,
    reward_name VARCHAR ( 50 ) NOT NULL,
    description TEXT,
    amount NUMERIC(10,2)
   
);

-- user_rewards linking table
CREATE TABLE IF NOT EXISTS user_rewards (
    reward_id INTEGER REFERENCES rewards(reward_id),
    user_id INTEGER REFERENCES users(user_id)
    -- CONSTRAINT user_rewards_pkey PRIMARY KEY(reward_id, user_id)
    -- removed constraint to allow multiple entries for same user
);

-- punishments table (withdraws from users bank_total)
CREATE TABLE IF NOT EXISTS punishments (
    -- punishment_id uuid DEFAULT uuid_generate_v4 (),
    punishment_id SERIAL PRIMARY KEY,
    punishment_name VARCHAR ( 50 ) NOT NULL,
    description TEXT,
    amount NUMERIC(10,2)
);

-- user_punishments linking table
CREATE TABLE IF NOT EXISTS user_punishments (
    punishment_id INTEGER REFERENCES punishments(punishment_id),
    user_id INTEGER REFERENCES users(user_id)
    -- CONSTRAINT user_punishments_pkey PRIMARY KEY(punishment_id, user_id)
    -- removed constraint to allow multiple entries for same user
);

-- REMOVING THE BANK TABLE TO GO A DIFFERENT ROUTE
-- CREATE TABLE IF NOT EXISTS bank (
--     -- bank_id uuid DEFAULT uuid_generate_v4 (),
--     bank_id SERIAL PRIMARY KEY,
--     account_holder_id INTEGER,
--     balance NUMERIC(10,2) DEFAULT 0.00,
--     CONSTRAINT fk_bank_account_holder
--         FOREIGN KEY (account_holder_id)   
--             REFERENCES users(user_id)
-- );

-- REMOVING THE TRANSACTIONS TABLE TO GO A DIFFERENT ROUTE
-- CREATE TABLE IF NOT EXISTS transactions (
--     transaction_id SERIAL PRIMARY KEY,
--     user_id INTEGER REFERENCES users,
--     completed_on TIMESTAMP,
--     reward_id INTEGER REFERENCES rewards,
--     chore_id INTEGER REFERENCES chores,
--     punishment_id INTEGER REFERENCES punishments,

-- )


-- REMOVING THE DEPOSITS TABLE TO GO A DIFFERENT ROUTE
-- CREATE TABLE IF NOT EXISTS deposits (
--     deposit_id SERIAL PRIMARY KEY,
--     user_id INTEGER REFERENCES users,
--     bank_id INTEGER REFERENCES bank,
--     deposit_amount NUMERIC(10,2) NOT NULL,
--     -- deposit amount based on Chores, Rewards and Punishment Amounts
--     CONSTRAINT fk_bank_deposit
--         FOREIGN KEY (deposit_amount)
--             REFERENCES 
-- )

--  initalize parents (with $60 each available)
INSERT INTO users(username, password, email, created_on, user_role, balance)
    VALUES
    ('dad', 'secret', 'dad@test.com', CURRENT_TIMESTAMP, 'parent', 60.00),
    ('mom', 'secret', 'mom@test.com', CURRENT_TIMESTAMP, 'parent', 60.00);

INSERT INTO users(username, password, email, created_on, user_role, balance)
    VALUES
    ('child1', 'secret', 'child1@test.com', CURRENT_TIMESTAMP, 'child', 0.00),
    ('child2', 'secret', 'child2@test.com', CURRENT_TIMESTAMP, 'child', 0.00),
    ('child3', 'secret', 'child3@test.com', CURRENT_TIMESTAMP, 'child', 0.00);
-- insert all the chores into the chores table

-- TODO: automatically assign a bank account to each user upon creating user
--  INSERT INTO bank all the init users and set balance to 0

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

-- assign chores to child1
INSERT INTO user_chores(chore_id, user_id, _status)
    VALUES
    (1, 3, 'assigned'),
    (4, 3, 'assigned'),
    (6, 3, '');

-- assign chores to child2
INSERT INTO user_chores(chore_id, user_id, _status)
    VALUES
    (3, 4, 'completed'),
    (2, 4, ''),
    (12, 4, '');

-- assign chores to child3
INSERT INTO user_chores(chore_id, user_id, _status)
    VALUES
    (7, 5. 'assigned'),
    (9, 5, ''),
    (14, 5, 'completed'),
    (11, 5, '');