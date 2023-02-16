-- create the table unique_id on MySQL Server using unique keyword on field

CREATE TABLE IF NOT EXISTS unique_id (
	   id INT DEFAULT 1 UNIQUE,
	   name VARCHAR(256)
);
