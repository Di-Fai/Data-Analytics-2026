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

-- -------------------------------------------------------------------------------------
USE northwind;


-- EX 25
SELECT OrderID, CustomerID, OrderDate
FROM orders
WHERE OrderDate = '1997-01-01';

-- EX 26
SELECT OrderID, OrderDate
FROM orders
WHERE YEAR(orderDate) = 1997
AND MONTH(OrderDate) = 6;

-- EX 27

SELECT ProductName, UnitPrice
FROM Products
ORDER BY UnitPrice DESC;

-- EX 28

SELECT CompanyName, Country
FROM Customers
ORDER BY Country ASC, CompanyName ASC;

 -- EX 29
 
 SELECT ProductName, UnitPrice
 FROM Products
 ORDER BY UnitPrice DESC
 LIMIT 5;
 
 -- EX 30
 
 SELECT ProductName, UnitPrice
 FROM Products
 ORDER BY UnitPrice DESC
 LIMIT 5, 5;
 
 -- EX 36
 
 Select ProductName, UnitPrice AS 'Original Price',
 UnitPrice - (UnitPrice * 0.10) AS '10% Discount Price'
 FROM Products;
 
 
 -- -------------------------- JOINS ----------------------------------
 
 -- EXE 1 
 
 SELECT o.OrderID, c.CompanyName AS 'Customer', o.Orderdate
 FROM Orders o
 JOIN Customers c 
 ON o.CustomerID = c.CustomerID
 ORDER BY o.OrderDate DESC
 LIMIT 5;
 
 -- EXE 2
 
 SELECT OrderID, CompanyName, OrderDate
 FROM Orders
 JOIN Customers USING (CustomerID)
 ORDER BY Orderdate
 LIMIT 5;
 
 -- EXE 3
 
 SELECT p.ProductName, c.CategoryName, p.UnitPrice
 FROM Products p
INNER JOIN categories c ON p.CategoryID = c.CategoryID
ORDER BY c.CategoryName, p.ProductName
LIMIT 6; 


SELECT p.ProductName, c.CategoryName, p.UnitPrice
 FROM Products p
INNER JOIN categories c USING (CategoryID)
ORDER BY c.CategoryName, p.ProductName
LIMIT 6;

-- EXE 5

SELECT c.CompanyName,
COUNT(o.OrderID) AS 'Order Count'
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.CompanyName
ORDER BY 'Order Count' ASC
LIMIT 5;

