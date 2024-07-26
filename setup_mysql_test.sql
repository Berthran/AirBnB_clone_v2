-- Prepares a MySQL server for the project

-- STEP 1: Create a database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- STEP 2: Add a new User
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- STEP 3: Grant all privileges to hbnb_test on hbnb_test_db database
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- STEP 4: Grant SELECT privilege to hbnb_test on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost'
