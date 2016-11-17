select countries.name, languages.language, languages.percentage 
from countries 
join languages on countries.id = languages.country_id
where language = 'slovene';

select countries.name , count(*) as cities
from cities 
left join countries on cities.country_id
order by cities desc; 

select countries.name, cities.population 
from countries
left join cities on countries.id = cities.country_id 
where countries.name = 'mexico' and cities.population>500000
order by cities.population desc; 

select countries.name, languages.percentage
from countries
left join languages on countries.id = country_id
where languages.percentage > 89
order by languages.percentage desc;

select countries.name, countries.surface_area, countries.population
from countries 
where countries.surface_area<501 and countries.population > 100000; 

select countries.name, countries.government_form, countries.capital, countries.life_expectancy
from countries
where countries.government_form='constitutional monarchy' and countries.capital > 200
and countries.life_expectancy>75;

select countries.name as country_name, cities.name as city_name, cities.district, cities.population 
from countries
left join cities on countries.id = cities.country_id
where cities.district='Buenos Aires' and cities.population>500000;

select countries.region, count(*) as countries
from countries group by region
order by countries desc;