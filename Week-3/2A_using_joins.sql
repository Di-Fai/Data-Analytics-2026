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
-- Create a single query to list the order id, ship name, ship address, and shipping company name of every order that shipped to Germany. Assign the shipping company
-- name the alias ‘Shipper.’ Order by the name of the shipper, then the name of who it shipped to
-- ---------------------------------------------------------------------------------------

SELECT o.OrderID, o.ShipName, o.ShipAddress, s.CompanyName AS 'Shipper'
FROM Orders o
JOIN Shippers s
ON o.ShipVia = s.ShipperID
WHERE o.ShipCountry = 'Germany'
ORDER BY s.CompanyName, o.ShipName;

-- -----------------------------------------------------------------------------------------------
-- Start from the same query as above (#4), but 
-- omit OrderID and add logic to group by ship name, with a count of how many orders were shipped for that ship name.
-- -------------------------------------------------------------------------------------

 SELECT o.ShipName, COUNT(*) AS OrderCount
 FROM Orders o
 JOIN Shippers s 
 ON o.ShipVia = s.ShipperID
 WHERE o.ShipCountry = 'Germany'
 GROUP BY o.ShipName
 ORDER BY o.ShipName;
 
 

