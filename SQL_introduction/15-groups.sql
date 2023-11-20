-- select all the same score in a table
SELECT score AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;