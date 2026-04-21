-- Nji Dimitri. K
-- April 20, 2026
-- SHOW DATABASE

use northwind;
SHOW TABLES;
SELECT ProductName, UnitPrice
FROM Products;
SELECT *
FROM products;


SELECT ProductName AS 'Product',
UnitPrice AS 'Price(USD)',
UnitsInStock AS 'Stock'
FROM Products;

-- Example 4: Using WHERE clause 
-- WHERE sets a condition to filter results 
-- Retrives all company names, cities, and country from Germany

SELECT CompanyName, City, Country
FROM customers
WHERE Country = 'Germany';

SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice > 50;


SELECT ProductName, UnitsInStock, ReorderLevel
FROM Products
WHERE UnitsInStock < ReorderLevel;

-- CONDITIONAL LOGIG EXAMPLES 

SELECT OrderID, Freight 
FROM orders 
WHERE Freight >= 100;


SELECT ProductName, UnitPrice, UnitsInStock 
FROM products 
WHERE UnitPrice > 20 
AND UnitsInStock > 50;

-- Come BAck Here
SELECT CompanyName, Country
FROM customers
WHERE Country IN ('UK', 'Ireland');

SELECT ProductName, CategoryID, UnitPrice
FROM products 
WHERE ( CategoryID = 1 OR CategoryID = 2  )
AND UnitPrice < 20;

SELECT CompanyName, Country
FROM Customers
WHERE Country  != 'USA';

SELECT ProductNAme, Discontinued
FROM products
WHERE Discontinued != 1;


SELECT CompanyName, Country
FROM customers
WHERE Country IN ('France', 'Germany', 'Spain');

SELECT ProductName, SupplierID
FROM Products
WHERE SupplierID NOT IN (1, 2, 3);


SELECT ProductName, UnitPrice
FROM Products
WHERE UnitPrice BETWEEN 10 AND 20;


SELECT OrderID, CustomerID, ShipRegion
FROM orders
WHERE ShipRegion IS null;

SELECT LastName, FirstName, Region
FROM employees
WHERE Region IS NOT null;

SELECT CompanyName
FROM Customers
WHERE CompanyName LIKE 'A%';

 
