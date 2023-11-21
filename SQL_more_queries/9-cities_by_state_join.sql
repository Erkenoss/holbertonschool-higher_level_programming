-- list all cities in database hbtn_0d_usa
SELECT cities.id, cities.name, states.name AS states
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id;