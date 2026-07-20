-- Question 1
-- Display the UserName, RestaurantName, and BillAmount for all orders.

SELECT
    u.UserName,
    r.RestaurantName,
    o.BillAmount
FROM Users u
JOIN Orders o
ON u.UserID = o.UserID
JOIN Restaurants r
ON o.RestaurantID = r.RestaurantID;


-- Question 2
-- Fetch a unique list of restaurant names that have orders and a delivery tracking record.

SELECT DISTINCT
    r.RestaurantName
FROM Restaurants r
JOIN Orders o
ON r.RestaurantID = o.RestaurantID
JOIN Deliveries d
ON o.OrderID = d.OrderID;


-- Question 3
-- Display OrderID and UserName where delivery took more than 35 minutes.

SELECT
    o.OrderID,
    u.UserName
FROM Users u
JOIN Orders o
ON u.UserID = o.UserID
JOIN Deliveries d
ON o.OrderID = d.OrderID
WHERE d.DeliveryTimeMinutes > 35;


-- Question 4
-- Find the total money spent by each user.

SELECT
    u.UserName,
    SUM(o.BillAmount) AS TotalSpent
FROM Users u
JOIN Orders o
ON u.UserID = o.UserID
GROUP BY
    u.UserName;


-- Question 5
-- Display every user along with the total number of orders they have placed. Include users with 0 orders.

SELECT
    u.UserName,
    COUNT(o.OrderID) AS OrderCount
FROM Users u
LEFT JOIN Orders o
ON u.UserID = o.UserID
GROUP BY
    u.UserID,
    u.UserName;


-- Question 6
-- Find restaurants whose total revenue from users living in Delhi is greater than ₹5000.

SELECT
    r.RestaurantName,
    SUM(o.BillAmount) AS TotalRevenue
FROM Restaurants r
JOIN Orders o
ON r.RestaurantID = o.RestaurantID
JOIN Users u
ON o.UserID = u.UserID
WHERE u.City = 'Delhi'
GROUP BY
    r.RestaurantID,
    r.RestaurantName
HAVING SUM(o.BillAmount) > 5000;


-- Question 7
-- Find restaurants that have cancelled orders along with the total number of cancelled orders.

SELECT
    r.RestaurantName,
    COUNT(*) AS CancelledOrders
FROM Restaurants r
JOIN Orders o
ON r.RestaurantID = o.RestaurantID
JOIN Deliveries d
ON o.OrderID = d.OrderID
WHERE d.DeliveryStatus = 'Cancelled'
GROUP BY
    r.RestaurantID,
    r.RestaurantName;


-- Question 8
-- Display the UserName and City of users whose single order amount is greater than the average order value.

SELECT
    u.UserName,
    u.City
FROM Users u
JOIN Orders o
ON u.UserID = o.UserID
WHERE o.BillAmount >
(
    SELECT AVG(BillAmount)
    FROM Orders
);


-- Question 9
-- Calculate the average delivery time for each cuisine where the restaurant's average rating is greater than 4.0.

SELECT
    r.Cuisine,
    AVG(d.DeliveryTimeMinutes) AS AverageDeliveryTime
FROM Restaurants r
JOIN Orders o
ON r.RestaurantID = o.RestaurantID
JOIN Deliveries d
ON o.OrderID = d.OrderID
GROUP BY
    r.Cuisine
HAVING AVG(r.Rating) > 4.0;


-- Question 10
-- Rank restaurants within each cuisine based on the total number of orders received (highest orders ranked 1st).

SELECT
    Cuisine,
    RestaurantName,
    OrderCount,
    RANK() OVER
    (
        PARTITION BY Cuisine
        ORDER BY OrderCount DESC
    ) AS RestaurantRank
FROM
(
    SELECT
        r.Cuisine,
        r.RestaurantName,
        COUNT(o.OrderID) AS OrderCount
    FROM Restaurants r
    LEFT JOIN Orders o
    ON r.RestaurantID = o.RestaurantID
    GROUP BY
        r.RestaurantID,
        r.RestaurantName,
        r.Cuisine
) AS RankedRestaurants;
