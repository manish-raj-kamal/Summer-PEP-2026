INSERT INTO Users VALUES
(1,'Aman Verma','Delhi','Premium'),
(2,'Riya Sen','Mumbai','Regular'),
(3,'Rahul Sharma','Delhi','Premium'),
(4,'Neha Gupta','Pune','Regular'),
(5,'Karan Singh','Delhi','Regular');

INSERT INTO Restaurants VALUES
(101,'Spice Symphony','North Indian',4.5),
(102,'Pizza Express','Italian',3.9),
(103,'Dragon House','Chinese',4.3),
(104,'Burger Point','Fast Food',4.2),
(105,'South Treat','South Indian',4.7);

INSERT INTO Orders VALUES
(501,1,101,1200.00,'2026-07-15'),
(502,2,102,450.00,'2026-07-16'),
(503,3,103,850.00,'2026-07-16'),
(504,1,104,600.00,'2026-07-17'),
(505,4,105,700.00,'2026-07-17'),
(506,5,101,1500.00,'2026-07-18'),
(507,3,105,950.00,'2026-07-18'),
(509,3,101,2500.00,'2026-07-20'),
(508,2,103,1100.00,'2026-07-19');

INSERT INTO Deliveries VALUES
(901,501,'Delivered',25),
(902,502,'Delivered',42),
(903,503,'Cancelled',30),
(904,504,'Delivered',40),
(905,505,'In-Transit',20),
(906,506,'Delivered',38),
(907,507,'Delivered',32),
(909,509,'Delivered',28),
(908,508,'Cancelled',45);
