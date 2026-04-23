USE Northwind;

-- 1a. Price of the cheapest item
-- ----------------------------------------------------------

SELECT MIN(UnitPrice) AS CheapestPrice
FROM Products;

-- 1b. Name of the product(s) with that cheapest price
-- --------------------------------------------------------------------------
SELECT ProductName
FROM Products
WHERE UnitPrice = (SELECT MIN(UnitPrice) FROM Products);

-- ---------------------------------------------------------------------------------
-- 2. Average price of all items
-- ------------------------------------------------------------------------------------

SELECT AVG(UnitPrice) AS AveragePrice
FROM Products;
-- Bonus: rounded to nearest cent

SELECT ROUND(AVG(UnitPrice), 2) AS AveragePrice
FROM Products;

-- 3a. Price of the most expensive item
-- --------------------------------------------------------------
SELECT MAX(UnitPrice) AS MostExpensivePrice
FROM Products;

-- 3b. Product name and supplier name for the product(s) with that price
-- --------------------------------------------------------------------------

SELECT p.ProductName, s.CompanyName AS SupplierName
FROM Products p
JOIN Suppliers s
ON p.SupplierID = s.SupplierID
WHERE p.UnitPrice = (SELECT MAX(UnitPrice) FROM Products);

-- -----------------------------------------------------------------------
-- 4. Total monthly payroll
-- -----------------------------------------------------------------------

SELECT SUM(Salary) AS TotalMonthlyPayroll
FROM Employees;

-- --------------------------------------------------------------
-- 5. Highest and lowest salary amounts
-- -----------------------------------------------------------

SELECT MAX(Salary) AS HighestSalary,
MIN(Salary) AS LowestSalary
FROM Employees;

-- -----------------------------------------------------------------------------
-- 6. Supplier name, supplier ID, and number of items they supply
-- ----------------------------------------------------------------------------

SELECT s.CompanyName AS SupplierName,
s.SupplierID,
COUNT(p.ProductID) AS NumberOfItems
FROM Suppliers s
LEFT JOIN Products p
ON s.SupplierID = p.SupplierID
GROUP BY s.CompanyName, s.SupplierID;

-- ---------------------------------------------------------------------------------
-- 7. Category names and average price of items in each category
-- --------------------------------------------------------------------------------------

SELECT c.CategoryName,
AVG(p.UnitPrice) AS AveragePrice
FROM Categories c
JOIN Products p
ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryName;

-- -------------------------------------------------------------------------------------
-- 8. Suppliers that provide at least 5 items
-- ---------------------------------------------------------------------------------------

SELECT s.CompanyName AS SupplierName,
COUNT(p.ProductID) AS NumberOfItems
FROM Suppliers s
JOIN Products p
ON s.SupplierID = p.SupplierID
GROUP BY s.CompanyName
HAVING COUNT(p.ProductID) >= 5;

-- -------------------------------------------------------------------------------------
-- 9. Products currently in inventory with inventory value
-- ------------------------------------------------------------------------------------------
SELECT ProductID,
ProductName,
UnitPrice * UnitsInStock AS InventoryValue
FROM Products
WHERE UnitsInStock > 0
ORDER BY InventoryValue DESC, ProductName ASC;
