-- script that list all cities of California that cna be found in the databse
-- hbtn_0d_usa
-- The states table contains only one record where name = California (but the id
-- can be different, as per the example)
-- Results must be sorted in ascending order by cities.id

SELECT c.id, c.name
	  FROM cities AS c, states AS s
WHERE c.state_id=s.id AND s.name = 'California'
	  ORDER BY c.id ASC;
