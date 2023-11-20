-- display all the score >= 10 and sort it by score
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;