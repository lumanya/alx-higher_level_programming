-- list the number of records with the smae score  in the table second_table

SELECT score, COUNT(score) AS number from second_table GROUP BY score
 ORDER BY score DESC;
