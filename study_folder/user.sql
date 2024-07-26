-- Viewing users
SELECT User, Host FROM mysql.user;

-- Checking active connections
SHOW PROCESSLIST;

-- Privileges and roles of a user
SHOW GRANTS FOR 'username'@'hostname';
