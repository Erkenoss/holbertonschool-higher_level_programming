-- list all the citie in a table
USE hbtn_0d_usa;

SELECT *
FROM cities
WHERE state_id = @california_id
ORDER BY id ASC;