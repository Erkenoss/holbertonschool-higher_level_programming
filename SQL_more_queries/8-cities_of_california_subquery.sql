-- list all the citie in a table
SELECT *
FROM hbtn_0d_usa.cities
WHERE state_id = @california_id
ORDER BY id ASC;