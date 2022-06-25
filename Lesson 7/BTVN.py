SELECT region, COUNT(name)
FROM countries
GROUP BY region

SELECT region, COUNT(DISTINCT subregion)
FROM countries
GROUP BY region

SELECT name
FROM countries
WHERE latitude < 0

SELECT region, count(DISTINCT currency)
FROM countries
GROUP BY region

SELECT name
FROM countries
where longitude BETWEEN -20 and 61

SELECT subregion
FROM countries
where longitude BETWEEN -20 and 61
GROUP BY subregion 