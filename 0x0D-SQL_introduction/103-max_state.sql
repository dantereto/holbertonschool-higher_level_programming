-- temperature
SELECT state, MAX(value) AS max_temp
FROM temperatures
GROUP BY city
ORDER BY max_temp DESC;
