-- displays average temperatures by city
SELECT city, ROUND(AVG(value), 4) AS avg_temp
FROM temperatures
GROUP BY city
ORDER_BY avg_temp DESC;
