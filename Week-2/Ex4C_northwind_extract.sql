# a) Products
# b)Categories

-- Question 5
USE northwind;
SELECT * FROM employees;
# The Northwind employee whoes name makes it look like she's a bird is Peacock Magaret.

-- Question 6
SELECT * FROM products;
# This query rerurns 77 records.
#To retrive only 10 rows using the toolbar, navigate to the row limit dropdown and change the row limit in the query pane toolbar to 10 and rerun the query.

SELECT * FROM products LIMIT 10;
# This query limits the results to 10 rows by using LIMIT 10.

-- Question 7
SELECT * FROM categories;
# The category id for Seafood is 8.

-- Question 8
SELECT OrderID, OrderDate, ShipName, ShipCountry FROM orders LIMIT 50;