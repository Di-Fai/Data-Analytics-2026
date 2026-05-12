/*
a) actor_id, first_name, last_name, last_update
b) film_id, title, description, release_year, language_id,original_language_id, rental_duration, rental_rate, length, replacement_cost, rating, special_features, last_update
c) film_actor table
d) This table includes feilds for rental_id, rental_date, inventory_id, customer_id, return_date, staff_id, last_update. this information on its own is hard to read because the table mostly uses ID numbers instead of names or file titles.
e) This table includes feilds for inventory_id, film_id, store_id, last_update
f) You need the rental, inventory, and film tables to understand the name of films that were rented on specific dates. 
-- The rental table shows the rental date and inventory_id
-- The inventory table connects inventory_id to film_id
-- The film table gives the film title 
*/

SELECT rental_date, inventory_id FROM rental;
SELECT inventory_id, film_id FROM inventory;
SELECT film_id, title FROM film;