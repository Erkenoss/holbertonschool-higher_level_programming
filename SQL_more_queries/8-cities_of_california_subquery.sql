-- list all the citie in a table
SELECT id, name
FROM cities
WHERE state_id = @california_id
ORDER BY id ASC;