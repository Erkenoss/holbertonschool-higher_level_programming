-- list all the citie in a table
SELECT *
FROM cities
WHERE state_id = @california_id
ORDER BY id ASC;