CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    City VARCHAR(50),
    Email VARCHAR(100)
);

-- Customer sample data
INSERT INTO Customers VALUES
(1,'Rahul Sharma','Delhi','rahul@gmail.com'),
(2,'Priya Nair','Chennai','priya@gmail.com'),
(3,'Arjun Kumar','Bangalore','arjun@gmail.com'),
(4,'Sneha Reddy','Hyderabad','sneha@gmail.com'),
(5,'Vikram Singh','Mumbai','vikram@gmail.com'),
(6,'Anjali Gupta','Pune','anjali@gmail.com'),
(7,'Rohit Verma','Delhi','rohit@gmail.com'),
(8,'Meera Iyer','Chennai','meera@gmail.com'),
(9,'Karan Patel','Ahmedabad','karan@gmail.com'),
(10,'Neha Joshi','Jaipur','neha@gmail.com'),
(11,'Amit Das','Kolkata','amit@gmail.com'),
(12,'Pooja Shah','Surat','pooja@gmail.com'),
(13,'Suresh Menon','Kochi','suresh@gmail.com'),
(14,'Deepa Rao','Bangalore','deepa@gmail.com'),
(15,'Manish Jain','Indore','manish@gmail.com');

CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Category VARCHAR(50),
    Price DECIMAL(10,2)
);

-- Product sample data
INSERT INTO Products VALUES
(101,'iPhone 15','Mobile',79999),
(102,'Samsung S24','Mobile',74999),
(103,'MacBook Air','Laptop',99999),
(104,'Dell Inspiron','Laptop',64999),
(105,'Boat Headphones','Accessories',1999),
(106,'Sony Headphones','Accessories',4999),
(107,'Apple Watch','Wearables',34999),
(108,'Samsung Watch','Wearables',29999),
(109,'HP Printer','Electronics',8999),
(110,'Logitech Mouse','Accessories',999),
(111,'Keyboard','Accessories',1499),
(112,'Tablet','Electronics',24999),
(113,'Office Chair','Furniture',12999),
(114,'Bluetooth Speaker','Accessories',3999),
(115,'Refrigerator','Home Appliances',45999);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    ProductID INT,
    Quantity INT,
    OrderDate DATE,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Order sample data
INSERT INTO Orders VALUES
(1001,1,101,1, DATE '2025-01-10'),
(1002,2,103,1, DATE '2025-01-12'),
(1003,3,105,2, DATE '2025-01-13'),
(1004,4,102,1, DATE '2025-01-15'),
(1005,5,107,1, DATE '2025-01-16'),
(1006,1,110,3, DATE '2025-01-18'),
(1007,7,104,1, DATE '2025-01-20'),
(1008,8,106,2, DATE '2025-01-21'),
(1009,2,111,1, DATE '2025-01-23'),
(1010,9,108,1, DATE '2025-01-25'),
(1011,10,112,1, DATE '2025-01-27'),
(1012,11,101,1, DATE '2025-01-28'),
(1013,12,109,1, DATE '2025-01-29'),
(1014,6,105,4, DATE '2025-01-30'),
(1015,3,110,2, DATE '2025-02-01'),
(1016,13,113,2, DATE '2025-02-02'),
(1017,14,114,3, DATE '2025-02-03'),
(1018,15,115,1, DATE '2025-02-04'),
(1019,14,103,1, DATE '2025-02-05'),
(1020,13,106,1, DATE '2025-02-06');

-- Revenue by city
select c.City, sum(p.Price * o.Quantity) as TotalRevenue
from Customers c
inner join orders o on c.CustomerID = o.CustomerID
inner join Products p on o.ProductID = p.ProductID
group by c.City
order by TotalRevenue desc;

-- Revenue by category
select p.category, sum(o.Quantity * p.Price) as TotalRevenue
from orders o
inner join Products p on o.ProductID = p.ProductID
group by p.Category
having TotalRevenue > 50000;

-- Customers buying above-average priced products
select c.CustomerID, c.CustomerName, p.ProductName, p.Price
from Customers c
inner join orders o on c.CustomerID = o.CustomerID
inner join Products p on p.ProductID = o.ProductID
where p.price > (select avg(price) from Products);

-- Order history view
create view OrderHistory as
select o.OrderID, c.CustomerName, p.ProductName, o.Quantity, o.OrderDate,
(o.Quantity * p.Price) as TotalRevenue
from Orders o
inner join Products p on o.ProductID = p.ProductID
inner join Customers c on c.CustomerID = o.CustomerID;

select * from OrderHistory;

-- Loyalty tier summary
select c.CustomerID, c.CustomerName, sum(o.Quantity * p.price) as TotalSpent,
case
  when sum(o.Quantity * p.price) >= 100000 then 'Platinum'
  when sum(o.Quantity * p.price) >= 50000 then 'Gold'
  else 'Silver'
end as LoyaltyTier
from Customers c
inner join Orders o on c.CustomerID = o.CustomerID
inner join Products p on p.ProductID = o.ProductID
group by CustomerID, CustomerName
order by TotalSpent desc;
