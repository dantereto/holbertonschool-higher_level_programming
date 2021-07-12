-- list all the recors
SELECT `score`, `name`
FROM `second_table`
WHERE name IS NOT NULL
ORDER BY `score` DESC;
