-- all the cities
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON states.id = cities.id
