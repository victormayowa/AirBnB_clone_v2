--  This script does the following:
-- Create or update the database hbnb_test_db
-- Create or update the user hbnb_test
-- Grant all privileges on the database hbnb_test_db to the user hbnb_test
-- Grant SELECT privilege on the database performance_schema to the user hbnb_test

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
