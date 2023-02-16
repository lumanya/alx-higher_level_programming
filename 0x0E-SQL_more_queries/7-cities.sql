-- create database hbtn_0d_usa if does not exists and table cities

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

/* create cities table */
CREATE TABLE IF NOT EXISTS cities (
	   PRIMARY KEY(id),
	   id		INT UNIQUE AUTO_INCREMENT NOT NULL,
	   state_id INT 	   				  NOT NULL,
	   name 	VARCHAR(256),
	   FOREIGN KEY (state_id) REFERENCES states(id)
);
