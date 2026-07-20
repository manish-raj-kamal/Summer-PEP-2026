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
