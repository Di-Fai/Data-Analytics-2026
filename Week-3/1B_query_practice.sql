USE northwind;

-- --------------------------------------------------------------------------------------------------------
-- Write a query to list the product id, product name, and unit price of every product that Northwind sells
-- --------------------------------------------------------------------------------------------------------

SELECT ProductID, ProductName, UnitPrice
FROM products;
-- Results return 77 rows

-- ----------------------------------------------------------------------------------------
-- Write a query to identify the products where the unit price is $7.50 or less
-- ------------------------------------------------------------------------------------------

SELECT ProductID, ProductName, UnitPrice
FROM products
WHERE UnitPrice <= 7.50;
-- Results return 5 rows

-- --------------------------------------------------------------------------------------------------------
-- What are the products that we carry where we have no units on hand, but 1 or more units are on backorder? Write a query that answers this question.
-- --------------------------------------------------------------------------------------------------------

SELECT ProductID, ProductName, UnitsInStock, UnitsOnOrder
FROM products
WHERE UnitsInStock = 0
AND UnitsOnOrder > 0;
-- Results return 1 row

-- -------------------------------------------------------------------------------------------------------
-- Examine the products table. How does it identify the type (category) of each item sold?
-- Where can you find a list of all categories? 
-- Write a set of queries to answer these questions, ending with a query that creates a list of all the seafood items we carry
-- ------------------------------------------------------------------------------------------------------------------

SELECT ProductID, ProductName, CategoryID
FROM products;
-- Results return 77 rows
-- CategoryID shows the category for every listed product

SELECT CategoryID, CategoryName
FROM categories;
-- Results return 8 rows
-- The category table sjows the category names 

SELECT p.ProductID, p.ProductName, c.CategoryName
FROM products p
JOIN categories c
ON p.CategoryID = c.CategoryID
WHERE c.CategoryName = 'Seafood';
-- Results return 8 rows
-- Products p and categoty c give the table aliases which can help to prevent any confusuin when two tables have similar column names when using the JOIN command

-- ----------------------------------------------------------------------------------------------------------------
-- Examine the products table again. How do you know what supplier each productcomes from?
-- Where can you find info on suppliers? 
-- Write a set of queries to find the specific identifier for "Tokyo Traders" and then find all products from that supplier
-- -------------------------------------------------------------------------------------------------------------------

SELECT SupplierID, ProductID, ProductName
FROM products;
-- Results return 77 rows

SELECT SupplierID, CompanyName, ContactName, City, Country
FROM suppliers;
-- Results return 29 rows
-- this supplier table shows suppliers details 

SELECT ProductID, ProductName, SupplierID
FROM products
WHERE SupplierID = (
SELECT SupplierID
FROM suppliers
WHERE CompanyName = 'Tokyo traders'
);
-- Results return 3 rows

-- ----------------------------------------------------------------------------------------------------------
-- How many employees work at northwind? 
-- What employees have "manager"somewhere in their job title? 
-- Write queries to answer each question.
-- ----------------------------------------------------------------------------------------------------------

SELECT COUNT(*) AS AllEmployees
FROM employees;
-- There are 9 employess at northwind

SELECT EmployeeID, FirstName, LastName, Title
FROM employees
WHERE Title LIKE '%manager%';
-- Results return 1 row. there is only one manger at northwind

