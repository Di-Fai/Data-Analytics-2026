USE northwind;

-- --------------------------------------------------------------------------------------
-- Create a single query to list the product id, product name, unit price and category name of all products. 
-- Order by category name and within that, by product name
-- -----------------------------------------------------------------------------------------------

SELECT p.ProductID, p.ProductName, p.UnitPrice, c.CategoryName
FROM Products p
Join Categories c
ON p.CategoryID = c.CategoryID
ORDER BY c.CategoryName, p.ProductName;

-- -------------------------------------------------------------------------------------------
-- Create a single query to list the product id, product name, unit price and supplier name of all products that cost more than $75. 
-- Order by product name
-- -----------------------------------------------------------------------------------------------------------

SELECT p.ProductID, p.ProductName, p.UnitPrice, s.CompanyName AS 'Supplier Name'
FROM Products p
JOIN Suppliers s 
ON p.SupplierID = s.SupplierID
WHERE UnitPrice > 75
ORDER BY p.ProductName;

-- ----------------------------------------------------------------------------------------------
-- Create a single query to list the product id, product name, unit price, category name, and supplier name of every product. 
-- Order by product name.
-- --------------------------------------------------------------------------------------------------------------------------

SELECT p.ProductID, p.ProductName, p.UnitPrice, c.CategoryName, s.CompanyName AS 'SupplierName'
FROM Products p
JOIN Categories c
ON p.CategoryID = c.CategoryID
JOIN Suppliers s
ON p.SupplierID = s.SupplierID
ORDER BY p.ProductName;

-- -------------------------------------------------------------------------------------

