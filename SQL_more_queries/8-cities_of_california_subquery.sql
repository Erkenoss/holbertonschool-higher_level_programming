-- list all the citie in a table
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROMM states WHERE name = 'California')
ORDER BY cities.id;