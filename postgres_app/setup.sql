DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS chores;
DROP TABLE IF EXISTS user_chores;
DROP TABLE IF EXISTS rewards;
DROP TABLE IF EXISTS user_rewards;
DROP TABLE IF EXISTS punishments;
DROP TABLE IF EXISTS user_punishments;

-- Originally was going to use UUID4 for all the IDs, but decided to scrap that and use SERIAL for now
-- This can be reimplemented after the database is connected (and working) with the FastAPI app

-- CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TYPE ROLES as ENUM ('child', 'parent'); -- could possibly change 'parent' to 'guardian' later on
CREATE TYPE CHORE_STATUS as ENUM ('assigned', 'completed');

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
    -- chore_id uuid PRIMARY KEY DEFAULT uuid_generate_v4 (),
    chore_id SERIAL PRIMARY KEY,
    chore_name VARCHAR ( 50 ) NOT NULL,
    description TEXT,
    amount NUMERIC(10,2)
);

-- user_chores linking table
CREATE TABLE IF NOT EXISTS user_chores (
    chore_id INTEGER REFERENCES chores(chore_id),
    user_id INTEGER REFERENCES users(user_id),
    chore_status CHORE_STATUS NOT NULL DEFAULT 'assigned',
    -- Timestamp not required if chore is set to 'assigned', 
    -- but will need to be present when chore_status is set to 'completed'
    completed_on TIMESTAMP,
    CONSTRAINT UC_user_chore UNIQUE (chore_id, user_id, chore_status, completed_on)
    -- if new assigned chore has no completed timestamp, a similar chore_id cannot be assigned to the user

    -- CONSTRAINT user_chores_pkey PRIMARY KEY(chore_id, user_id)
    -- removed constraint to allow multiple entries for same user
);


-- rewards table (withdraws from users bank_total)
CREATE TABLE IF NOT EXISTS rewards (
    -- reward_id uuid PRIMARY KEY DEFAULT uuid_generate_v4 (),
    reward_id SERIAL PRIMARY KEY,
    reward_name VARCHAR ( 50 ) NOT NULL,
    description TEXT,
    amount NUMERIC(10,2)
   
);

-- user_rewards linking table
CREATE TABLE IF NOT EXISTS user_rewards (
    reward_id INTEGER REFERENCES rewards(reward_id),
    user_id INTEGER REFERENCES users(user_id),
    completed_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT UC_user_reward UNIQUE (reward_id, user_id, completed_on)
    -- Unique constraint prevents double assigning to user_id
    -- completed_on in not null, compared to the user_chore.completed_on, which is nullable

    -- CONSTRAINT user_rewards_pkey PRIMARY KEY(reward_id, user_id)
    -- removed constraint to allow multiple entries for same user
);

-- punishments table (withdraws from users bank_total)
CREATE TABLE IF NOT EXISTS punishments (
    -- punishment_id uuid PRIMARY KEY DEFAULT uuid_generate_v4 (),
    punishment_id SERIAL PRIMARY KEY,
    punishment_name VARCHAR ( 50 ) NOT NULL,
    description TEXT,
    amount NUMERIC(10,2)
);

-- user_punishments linking table
CREATE TABLE IF NOT EXISTS user_punishments (
    punishment_id INTEGER REFERENCES punishments(punishment_id),
    user_id INTEGER REFERENCES users(user_id),
    completed_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT UC_user_punishment UNIQUE (punishment_id, user_id, completed_on)
    -- Unique constraint prevents double assigning to user_id
    -- completed_on in not null, compared to the user_chore.completed_on, which is nullable

    -- CONSTRAINT user_punishments_pkey PRIMARY KEY(punishment_id, user_id)
    -- removed constraint to allow multiple entries for same user
);

-- user balances
CREATE TABLE IF NOT EXISTS user_balances (
    username VARCHAR ( 50 ) NOT NULL,
    amount NUMERIC(10,2),
    balance NUMERIC(10, 2),
    completed_on TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

--  initalize parents (with $60 each available)
INSERT INTO users(username, password, email, created_on, user_role, balance)
    VALUES
    ('DAD', 'secret', 'dad@test.com', CURRENT_TIMESTAMP, 'parent', 60.00),
    ('MOM', 'secret', 'mom@test.com', CURRENT_TIMESTAMP, 'parent', 60.00);

INSERT INTO users(username, password, email, created_on, user_role, balance)
    VALUES
    ('CHILD1', 'secret', 'child1@test.com', CURRENT_TIMESTAMP, 'child', 0.00),
    ('CHILD2', 'secret', 'child2@test.com', CURRENT_TIMESTAMP, 'child', 0.00),
    ('CHILD3', 'secret', 'child3@test.com', CURRENT_TIMESTAMP, 'child', 0.00);
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


-- insert rewards (purchase rewards with money earned from chores)
INSERT INTO rewards(reward_name, description, amount)
    VALUES('Xbox Time', 'In-fighting with sibling(s)', -2.00),
    ('Dollar Store Trip', 'Purchase 1 item at the dollar store', -1.00),
    ('$10 Cash', 'Convert your in-app balance to IRL cash', -10.00),
    ('Movie Night', 'You pick a movie and the candy', -5.00),
    ('Fiesta Fun', 'Take a trip to ride go-carts or whatever you want', -20.00),
    ('Clothes Shopping', 'Get a new item of clothing (online or in a store)', -15.00),
    ('$10 Giftcard', 'Get a $10 Giftcard to somewhere', -10.00),
    ('Video Game', 'Buy a new video game', -40.00),
    ('Date with Parent(s)', 'Take Mom and/or Dad to a place of your choosing', -25.00),
    ('Ice Cream Party', 'Ice Cream, Toppings and Friends', -30.00);

-- create a view to query all users completed chores
CREATE VIEW completed_chores AS 
SELECT chores.*, users.username, users.balance, user_chores.chore_status, user_chores.completed_on
FROM chores
INNER JOIN user_chores
ON chores.chore_id = user_chores.chore_id
INNER JOIN users
ON user_chores.user_id = users.user_id
WHERE user_chores.chore_status='completed';


-- create a view to query all users assigned chores
CREATE VIEW assigned_chores AS 
SELECT chores.*, users.username, users.balance, user_chores.chore_status, user_chores.completed_on
FROM chores
INNER JOIN user_chores
ON chores.chore_id = user_chores.chore_id
INNER JOIN users
ON user_chores.user_id = users.user_id
WHERE user_chores.chore_status='assigned';

-- create view to query all users punishments
CREATE VIEW all_punishments AS
SELECT punishments.*, users.username, users.balance, user_punishments.completed_on
FROM punishments
INNER JOIN user_punishments
ON punishments.punishment_id = user_punishments.punishment_id
INNER JOIN users
ON user_punishments.user_id = users.user_id;

-- create view to query all users rewards
CREATE VIEW all_rewards AS
SELECT rewards.*, users.username, users.balance, user_rewards.completed_on
FROM rewards
INNER JOIN user_rewards
ON rewards.reward_id = user_rewards.reward_id
INNER JOIN users
ON user_rewards.user_id = users.user_id;


DO $$
DECLARE
-- declare username and user_id variables
set_username varchar;
set_uid integer;
set_cid integer;
BEGIN
-- set variables for username, uid, and cid
set_username := 'child1';
set_cid := 1;
set_uid := 3;

-- assign chores to child1, child2 and child3
INSERT INTO user_chores(chore_id, user_id, chore_status, completed_on)
    VALUES  (set_cid, set_uid, 'assigned', NULL);
-- insert recent values
INSERT INTO user_balances (username, amount, balance)
SELECT username, amount, balance
FROM completed_chores
WHERE chore_id=set_cid
AND username=set_username; 

END $$;

DO $$
DECLARE
-- declare username and user_id variables
set_username varchar;
set_uid integer;
set_cid integer;
BEGIN
set_cid := 4;
set_uid := 3;
set_username := 'child1';
INSERT INTO user_chores(chore_id, user_id, chore_status, completed_on)
    VALUES  (set_cid, set_uid, 'completed', CURRENT_TIMESTAMP);
-- insert recent values
INSERT INTO user_balances (username, amount, balance)
SELECT username, amount, balance
FROM completed_chores
WHERE chore_id=set_cid
AND username=set_username; 
END $$;


DO $$
DECLARE
-- declare username and user_id variables
set_username varchar;
set_uid integer;
set_cid integer;
BEGIN
set_cid := 6;
set_uid := 3;
set_username := 'child1';
INSERT INTO user_chores(chore_id, user_id, chore_status, completed_on)
    VALUES  (set_cid, set_uid, 'completed', CURRENT_TIMESTAMP);
-- insert recent values
INSERT INTO user_balances (username, amount, balance)
SELECT username, amount, balance
FROM completed_chores
WHERE chore_id=set_cid
AND username=set_username; 
END $$;


DO $$
DECLARE
-- declare username and user_id variables
set_username varchar;
set_uid integer;
set_cid integer;
BEGIN
set_username := 'child2';
set_cid := 3;
set_uid := 4;
INSERT INTO user_chores(chore_id, user_id, chore_status, completed_on)
    VALUES  (set_cid, set_uid, 'completed', CURRENT_TIMESTAMP);
-- insert recent values
INSERT INTO user_balances (username, amount, balance)
SELECT username, amount, balance
FROM completed_chores
WHERE chore_id=set_cid
AND username=set_username; 
END $$;

DO $$
DECLARE
-- declare username and user_id variables
set_username varchar;
set_uid integer;
set_cid integer;
BEGIN
set_cid := 2;
set_uid := 4;
set_username := 'child2';
INSERT INTO user_chores(chore_id, user_id, chore_status, completed_on)
    VALUES  (set_cid, set_uid, 'completed', CURRENT_TIMESTAMP);
-- insert recent values
INSERT INTO user_balances (username, amount, balance)
SELECT username, amount, balance
FROM completed_chores
WHERE chore_id=set_cid
AND username=set_username; 
END $$;


DO $$
DECLARE
-- declare username and user_id variables
set_username varchar;
set_uid integer;
set_cid integer;
BEGIN
set_uid := 4;
set_username := 'child2';
set_cid := 12;
INSERT INTO user_chores(chore_id, user_id, chore_status, completed_on)
    VALUES  (set_cid, set_uid, 'completed', CURRENT_TIMESTAMP);
-- insert recent values
INSERT INTO user_balances (username, amount, balance)
SELECT username, amount, balance
FROM completed_chores
WHERE chore_id=set_cid
AND username=set_username; 
END $$;

DO $$
DECLARE
-- declare username and user_id variables
set_username varchar;
set_uid integer;
set_cid integer;
BEGIN
set_uid := 5;
set_username := 'child3';
set_cid := 7;
INSERT INTO user_chores(chore_id, user_id, chore_status, completed_on)
    VALUES  (set_cid, set_uid, 'completed', CURRENT_TIMESTAMP);
-- insert recent values
INSERT INTO user_balances (username, amount, balance)
SELECT username, amount, balance
FROM completed_chores
WHERE chore_id=set_cid
AND username=set_username; 
END $$;

DO $$
DECLARE
-- declare username and user_id variables
set_username varchar;
set_uid integer;
set_cid integer;
BEGIN
set_uid := 5;
set_username := 'child3';
set_cid := 9;
INSERT INTO user_chores(chore_id, user_id, chore_status, completed_on)
    VALUES  (set_cid, set_uid, 'completed', CURRENT_TIMESTAMP);
-- insert recent values
INSERT INTO user_balances (username, amount, balance)
SELECT username, amount, balance
FROM completed_chores
WHERE chore_id=set_cid
AND username=set_username; 
END $$;

DO $$
DECLARE
-- declare username and user_id variables
set_username varchar;
set_uid integer;
set_cid integer;
BEGIN
set_uid := 5;
set_username := 'child3';
set_cid := 14;
INSERT INTO user_chores(chore_id, user_id, chore_status, completed_on)
    VALUES  (set_cid, set_uid, 'completed', CURRENT_TIMESTAMP);
-- insert recent values
INSERT INTO user_balances (username, amount, balance)
SELECT username, amount, balance
FROM completed_chores
WHERE chore_id=set_cid
AND username=set_username; 
END $$;

DO $$
DECLARE
-- declare username and user_id variables
set_username varchar;
set_uid integer;
set_cid integer;
BEGIN
set_uid := 5;
set_username := 'child3';
set_cid :=11;
INSERT INTO user_chores(chore_id, user_id, chore_status, completed_on)
    VALUES  (set_cid, set_uid, 'completed', CURRENT_TIMESTAMP);
-- insert recent values
INSERT INTO user_balances (username, amount, balance)
SELECT username, amount, balance
FROM completed_chores
WHERE chore_id=set_cid
AND username=set_username; 
END $$;


-- assign rewards to child1, child2 and child3
INSERT INTO user_rewards(reward_id, user_id)
    VALUES (1, 3);
-- insert recent values
INSERT INTO user_balances (username, amount, balance)
SELECT username, amount, balance
FROM all_rewards
WHERE reward_id=1
AND username='child1'; 

INSERT INTO user_rewards(reward_id, user_id)
    VALUES (4, 3);
-- insert recent values
INSERT INTO user_balances (username, amount, balance)
SELECT username, amount, balance
FROM all_rewards
WHERE reward_id=1
AND username='child1'; 

INSERT INTO user_rewards(reward_id, user_id)
    VALUES (6, 3);
-- insert recent values
INSERT INTO user_balances (username, amount, balance)
SELECT username, amount, balance
FROM all_rewards
WHERE reward_id=1
AND username='child1'; 

INSERT INTO user_rewards(reward_id, user_id)
    VALUES (3, 4);

-- insert recent values
INSERT INTO user_balances (username, amount, balance)
SELECT username, amount, balance
FROM all_rewards
WHERE reward_id=1
AND username='child1'; 

INSERT INTO user_rewards(reward_id, user_id)
    VALUES (2, 4);
-- insert recent values
INSERT INTO user_balances (username, amount, balance)
SELECT username, amount, balance
FROM all_rewards
WHERE reward_id=1
AND username='child1'; 

INSERT INTO user_rewards(reward_id, user_id)
    VALUES (4, 4);
-- insert recent values
INSERT INTO user_balances (username, amount, balance)
SELECT username, amount, balance
FROM all_rewards
WHERE reward_id=1
AND username='child1'; 

INSERT INTO user_rewards(reward_id, user_id)
    VALUES (4, 5);
-- insert recent values
INSERT INTO user_balances (username, amount, balance)
SELECT username, amount, balance
FROM all_rewards
WHERE reward_id=1
AND username='child1'; 

INSERT INTO user_rewards(reward_id, user_id)
    VALUES (2, 5);
-- insert recent values
INSERT INTO user_balances (username, amount, balance)
SELECT username, amount, balance
FROM all_rewards
WHERE reward_id=1
AND username='child1'; 

INSERT INTO user_rewards(reward_id, user_id)
    VALUES (5, 5);
-- insert recent values
INSERT INTO user_balances (username, amount, balance)
SELECT username, amount, balance
FROM all_rewards
WHERE reward_id=1
AND username='child1'; 

INSERT INTO user_rewards(reward_id, user_id)
    VALUES (10, 5);
-- insert recent values
INSERT INTO user_balances (username, amount, balance)
SELECT username, amount, balance
FROM all_rewards
WHERE reward_id=1
AND username='child1'; 

-- assign punishments to child1, child2 and child3
INSERT INTO user_punishments(punishment_id, user_id)
    VALUES (6, 3);
-- insert recent values
INSERT INTO user_balances (username, amount, balance)
SELECT username, amount, balance
FROM all_punishments
WHERE punishment_id=1
AND username='child1'; 

INSERT INTO user_punishments(punishment_id, user_id)
    VALUES (7, 3);
-- insert recent values
INSERT INTO user_balances (username, amount, balance)
SELECT username, amount, balance
FROM all_punishments
WHERE punishment_id=1
AND username='child1'; 

INSERT INTO user_punishments(punishment_id, user_id)
    VALUES (1, 4);
-- insert recent values
INSERT INTO user_balances (username, amount, balance)
SELECT username, amount, balance
FROM all_punishments
WHERE punishment_id=1
AND username='child1'; 

INSERT INTO user_punishments(punishment_id, user_id)
    VALUES (9, 4);
-- insert recent values
INSERT INTO user_balances (username, amount, balance)
SELECT username, amount, balance
FROM all_punishments
WHERE punishment_id=1
AND username='child1'; 

INSERT INTO user_punishments(punishment_id, user_id)
    VALUES (1, 5);
-- insert recent values
INSERT INTO user_balances (username, amount, balance)
SELECT username, amount, balance
FROM all_punishments
WHERE punishment_id=1
AND username='child1'; 

INSERT INTO user_punishments(punishment_id, user_id)
    VALUES (6, 3);
-- insert recent values
INSERT INTO user_balances (username, amount, balance)
SELECT username, amount, balance
FROM all_punishments
WHERE punishment_id=1
AND username='child1'; 

INSERT INTO user_punishments(punishment_id, user_id)
    VALUES (5, 5);
-- insert recent values
INSERT INTO user_balances (username, amount, balance)
SELECT username, amount, balance
FROM all_punishments
WHERE punishment_id=1
AND username='child1'; 

INSERT INTO user_punishments(punishment_id, user_id)
    VALUES (2, 5);
-- insert recent values
INSERT INTO user_balances (username, amount, balance)
SELECT username, amount, balance
FROM all_punishments
WHERE punishment_id=1
AND username='child1'; 



-- Update users balance ONLY for COMPLETED chores
UPDATE users
SET balance= users.balance+chores.amount
FROM chores, user_chores
WHERE chores.chore_id=user_chores.chore_id
AND users.user_id=user_chores.user_id
AND user_chores.chore_status = 'completed';

-- Update user balance for ALL rewards
UPDATE users
SET balance= users.balance+rewards.amount
FROM rewards, user_rewards
WHERE rewards.reward_id=user_rewards.reward_id
AND users.user_id=user_rewards.user_id;

-- Update user balance for ALL punishments
UPDATE users
SET balance= users.balance+punishments.amount
FROM punishments, user_punishments
WHERE punishments. punishment_id=user_punishments.punishment_id
AND users.user_id=user_punishments.user_id;