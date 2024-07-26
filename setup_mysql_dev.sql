-- Prepares a MySQL server for the project

-- STEP 1: Create a database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- STEP 2: Add a new User
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- STEP 3: Grant all privileges to hbnb_dev on hbnb_dev_db database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- STEP 4: Grant SELECT privilege to hbnb_dev on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost'
