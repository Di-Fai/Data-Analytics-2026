USE northwind;

-- EXE 1
SELECT ProductID, ProductName, UnitsInStock
FROM products
ORDER BY UnitPrice DESC;

-- EXE 2 
SELECT CustomerID, CompanyName, ContactName, Country
FROM Customers
ORDER BY Country ASC, CompanyName ASC;

-- EXE 3 
SELECT CategoryID, 
COUNT(ProductID) AS ProductCount
FROM products
GROUP BY CategoryID
ORDER BY ProductCount DESC;

-- 4
SELECT OrderID,
ROUND(SUM(UnitPrice * Quantity * (1 - Discount)), 2) AS Revenue
FROM `Order Details`
GROUP BY OrderID
ORDER BY Revenue DESC;

