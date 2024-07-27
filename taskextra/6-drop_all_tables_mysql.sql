-- Step 1: Initialize the variable
SET @tables = NULL;

-- Step 2: Generate the list of tables and assign to the variable
SELECT GROUP_CONCAT('`', table_name, '`') INTO @tables
FROM information_schema.tables 
WHERE table_schema = 'your_database_name';

-- Step 3: Check the contents of the variable
SELECT @tables;

-- Step 4: Create the DROP TABLE statement and assign to the variable
SET @tables = CONCAT('DROP TABLE IF EXISTS ', @tables);

-- Step 5: Check the contents of the variable
SELECT @tables;

-- Step 6: Prepare and execute the statement
PREPARE stmt FROM @tables;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

