USE northwind;

-- 1. Product name(s) of the most expensive products
-- ---------------------------------------------------------

SELECT ProductName
FROM Products
WHERE UnitPrice = (
SELECT MAX(UnitPrice)
FROM Products
);

-- 2. Product name(s) and category of the least expensive products
-- ------------------------------------------------------------------------

SELECT p.ProductName, c.CategoryName
FROM Products p
JOIN Categories c
ON p.CategoryID = c.CategoryID
WHERE p.UnitPrice = (
SELECT MIN(UnitPrice)
FROM Products
);

-- 3. Order id, shipping name, and shipping address of all orders
-- shipped via "Federal Shipping"
-- -----------------------------------------------------------------------
SELECT OrderID, ShipName, ShipAddress
FROM Orders
WHERE ShipVia = (
SELECT ShipperID
FROM Shippers
WHERE CompanyName = 'Federal Shipping'
);

-- 4. Order ids of the orders that included "Sasquatch Ale"
-- ------------------------------------------------------------------------

SELECT DISTINCT OrderID
FROM OrderDetails
WHERE ProductID = (
SELECT ProductID
FROM Products
WHERE ProductName = 'Sasquatch Ale'
);

-- 5. Name of the employee that sold order 10266
-- ----------------------------------------------------------------------------

SELECT FirstName, LastName
FROM Employees
WHERE EmployeeID = (
SELECT EmployeeID
FROM Orders
WHERE OrderID = 10266
);


-- 6. Name of the customer that bought order 10266
-- ----------------------------------------------------------------------

SELECT CompanyName
FROM Customers
WHERE CustomerID = (
SELECT CustomerID
FROM Orders
WHERE OrderID = 10266
);


SELECT ContactName
FROM Customers
WHERE CustomerID = (
SELECT CustomerID
FROM Orders
WHERE OrderID = 10266
);