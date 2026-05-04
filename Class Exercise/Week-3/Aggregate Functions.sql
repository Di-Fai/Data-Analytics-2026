USE sakila;

 -- Using COUNT()
 
SELECT COUNT(*) 
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE c.name = 'Action';

-- Using COUNT(DISTINCT column_name)

SELECT COUNT(DISTINCT country) 
FROM country;

-- Summing data with SUM()

SELECT SUM(amount) 
FROM payment;

-- ----------------------------------------------------------------------
-- Using GROUP BY

SELECT customer_id, SUM(amount) 
FROM payment
GROUP BY customer_id;

--  Combining with other functions

SELECT AVG(amount), SUM(amount) 
FROM payment;

-- Finding averages with AVG()

SELECT AVG(length) 
FROM film;


--  Working with GROUP BY

SELECT customer_id, AVG(amount) 
FROM payment
GROUP BY customer_id;


-- Identifying extremes with MIN() and MAX()

SELECT MIN(release_year) 
FROM film;

-- Working with Group By

SELECT category_id, MIN(f.rental_rate) AS min_rental_rate
FROM film f
JOIN film_category fc
ON f.film_id = fc.film_id
GROUP BY fc.category_id;

-- Using MAX 

SELECT customer_id, MAX(amount) 
FROM payment
GROUP BY customer_id;







-- WHat was each customers total, average, minimum and maximum payment amount 

SELECT p.customer_id, c.first_name,
SUM(amount) AS Total_Paid,
AVG(amount) AS Average_Payment,
MIN(amount) AS Smallest_Payment,
MAX(amount) AS Largest_Payment
FROM payment p
JOIN customer c
ON p.customer_id = c.customer_id
GROUP BY p.customer_id, c.first_name;



