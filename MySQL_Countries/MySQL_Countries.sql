-- 1. What query would you run to get all the countries that speak Slovene? Your query should return the name of the country, language and language percentage. Your query should arrange the result by language percentage in descending order. (1)

SELECT  *
FROM countries AS c JOIN languages AS l 
ON c.id = l.country_id
WHERE l.language = 'Slovene';


-- 2. What query would you run to display the total number of cities for each country? Your query should return the name of the country and the total number of cities. Your query should arrange the result by the number of cities in descending order. (3)
SELECT con.name, cit.cities, COUNT(*) as Total_Number_Of_Cities
FROM countries AS con JOIN cities AS cit
ON con.id = cit.country_id
GROUP BY con.name
ORDER BY con.name DESC;

-- 3. What query would you run to get all the cities in Mexico with a population of greater than 500,000? Your query should arrange the result by population in descending order. (1)
SELECT cit.name, cit.population
FROM countries AS con JOIN cities AS cit
ON con.id = cit.country_id
WHERE con.name='Mexico' and cit.population=500000;

-- 4. What query would you run to get all languages in each country with a percentage greater than 89%? Your query should arrange the result by percentage in descending order. (1)
SELECT  c.name, l.language, l.percentage
FROM countries AS c JOIN languages AS l 
ON c.id = l.country_id
WHERE l.percentage> 89
ORDER BY l.percentage DESC;

-- 5. What query would you run to get all the countries with Surface Area below 501 and Population greater than 100,000? (2)
SELECT con.name, cit.population, con.surface_area
FROM countries AS con JOIN cities AS cit
ON con.id = cit.country_id
WHERE con.surface_area<501 and cit.population>100000;

-- 6. What query would you run to get countries with only Constitutional Monarchy with a capital greater than 200 and a life expectancy greater than 75 years? (1)
SELECT government_form, capital, life_expectancy
FROM countries
WHERE capital>200 and life_expectancy>75;

-- 7. What query would you run to get all the cities of Argentina inside the Buenos Aires district and have the population greater than 500, 000? The query should return the Country Name, City Name, District and Population. (2)
SELECT con.name, cit.name, cit.population, cit.district
FROM countries AS con JOIN cities AS cit
ON con.id = cit.country_id
WHERE cit.population > 500000 and con.distict='Buenos Aires district';

-- 8. What query would you run to summarize the number of countries in each region? The query should display the name of the region and the number of countries. Also, the query should arrange the result by the number of countries in descending order. (2)
SELECT region, COUNT(*) as countries
FROM countries
GROUP BY region
ORDER BY region DESC;

