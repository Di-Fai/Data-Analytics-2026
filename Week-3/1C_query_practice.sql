USE northwind;

-- -------------------------------------------------------------------------------------------------
-- 1. List product id, product name, and unit price of every product in ascending order by price
-- ------------------------------------------------------------------------------------------------

SELECT ProductID, ProductName, UnitPrice
FROM products
ORDER BY UnitPrice ASC;

-- --------------------------------------------------------------------------------------------------
-- 2. Products with at least 100 units on hand, ordered by price descending
-- ------------------------------------------------------------------------------------------------
SELECT ProductID, ProductName, UnitsInStock, UnitPrice
FROM products
WHERE UnitsInStock >= 100
ORDER BY UnitPrice DESC;

-- ------------------------------------------------------------------------------------------------------------
-- 3. Products with at least 100 units on hand, ordered by price descending,
-- and if prices are the same, by product name ascending
-- --------------------------------------------------------------------------------------------------------------

SELECT ProductID, ProductName, UnitsInStock, UnitPrice
FROM products
WHERE UnitsInStock >= 100
ORDER BY UnitPrice DESC, ProductName ASC;

-- --------------------------------------------------------------------------------------------------------
-- 4. Total number of distinct customers who have placed orders
-- --------------------------------------------------------------------------------------------------------

SELECT COUNT(DISTINCT CustomerID) AS CustomerCount
FROM orders;

-- --------------------------------------------------------------------------------------------------------
-- 5. Total number of distinct customers who have placed orders for each ship country
-- --------------------------------------------------------------------------------------------------------

SELECT ShipCountry, COUNT(DISTINCT CustomerID) AS CustomerCount
FROM orders
GROUP BY ShipCountry
ORDER BY CustomerCount DESC;

-- ------------------------------------------------------------------------------------------------------------
-- 6. Products with less than 25 units in stock but 1 or more units on order
--  --------------------------------------------------------------------------------------------------------

SELECT ProductID, ProductName, UnitsInStock, UnitsOnOrder
FROM products
WHERE UnitsInStock < 25
AND UnitsOnOrder >= 1
ORDER BY UnitsOnOrder DESC, ProductName ASC;

-- ---------------------------------------------------------------------------------------------------
-- 7. Each job title with a count of employees holding that title
-- ----------------------------------------------------------------------------------------------------

SELECT Title, COUNT(*) AS EmployeeCount
FROM employees
GROUP BY Title;

-- ------------------------------------------------------------------------------------------------------
-- 8. Employees with a monthly salary between 2000 and 2500, ordered by job title
-- -----------------------------------------------------------------------------------------------------
SELECT EmployeeID, FirstName, LastName, Title, Salary
FROM employees
WHERE Salary BETWEEN 2000 AND 2500
ORDER BY Title ASC;-- 8. Employees with a monthly salary between 2000 and 2500, ordered by job title
SELECT EmployeeID, FirstName, LastName, Title, Salary
FROM employees
WHERE Salary BETWEEN 2000 AND 2500
ORDER BY Title ASC;