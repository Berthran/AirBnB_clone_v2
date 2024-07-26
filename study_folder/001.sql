-- Create MySQL user and grant it privileges
CREATE USER 'dan1234'@'localhost' IDENTIFIED BY 'Dan1234###';
GRANT ALL PRIVILEGES ON hbtn_0e_0_usa.* TO 'dan1234'@'localhost';
FLUSH PRIVILEGES;
