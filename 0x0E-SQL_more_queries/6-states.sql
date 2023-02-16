-- create the database hbtn_0d_usa and the table states in theta database
-- states description:

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

/* creating table */
CREATE TABLE IF NOT EXISTS states (
	   PRIMARY KEY (id),
	   id 	INT	UNIQUE AUTO_INCREMENT NOT NULL,
	   name VARCHAR(256)
);
