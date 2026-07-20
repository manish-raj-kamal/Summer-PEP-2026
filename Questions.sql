SECTION A:
  Question 1
  ● Problem Statement: Write a query to display the UserName of the customer, the
  RestaurantName they ordered from, and the BillAmount for all orders.
  ● Tables to Use: Users, Restaurants, Orders
    
  Question 2
  ● Problem Statement: Fetch a unique list of all restaurant names that have
  successfully had orders cooked and assigned to a delivery tracking record (even
  if the delivery was later cancelled).
  ● Tables to Use: Restaurants, Orders
    
  Question 3
  ● Problem Statement: Display all OrderID logs along with their corresponding
  user names where the order took more than 35 minutes to deliver.
  ● Tables to Use: Users, Orders, Deliveries
  
  Question 4
  ● Problem Statement: Find the total money spent (BillAmount) on food delivery
  orders by each individual UserName. Display the user name and their total
  spend amount.
  ● Tables to Use: Users, Orders

  
SECTION B:
  Question 5
  ● Problem Statement: The business intelligence team needs to see a
  comprehensive dispatch chart. Write a query to list every user name registered
  on the system along with the total number of orders they have placed. If a user
  has placed 0 orders, their name must still appear in the list with an order count of
  0.
  ● Tables to Use: Users, Orders
    
  Question 6
  ● Problem Statement: Write a query to find the names of restaurants that have
  generated a total cumulative revenue (sum of BillAmount) greater than ₹5,000
  from users who live specifically in the city of 'Delhi'.
  ● Tables to Use: Users, Restaurants, Orders
    
  Question 7
  ● Problem Statement: Identify structural system inefficiencies. Write a query to
  find the names of all restaurants that have suffered from 'Cancelled' orders, along
  with the total count of cancelled orders each restaurant faced.
  ● Tables to Use: Restaurants, Orders, Deliveries


SECTION C:
  Question 8
  ● Problem Statement: Write a query to find the UserName and Email/City profiles
  of users who have spent more money on a single order than the average order
  value computed across the entire platform.
  ● Tables to Use: Users, Orders
    
  Question 9
  ● Problem Statement: Generate a platform-wide operational efficiency audit
  report. Write a query to calculate the average delivery time
  (DeliveryTimeMinutes) for each distinct Cuisine category offered on the
  platform, but only include cuisines where the restaurant average rating is strictly
  above 4.0.
  ● Tables to Use: Restaurants, Orders, Deliveries
    
  Question 10
  ● Problem Statement: Write a query to rank restaurants within each unique
  Cuisine category based on the total number of orders they have received
  (highest orders ranked 1st). The output should show the Cuisine, Restaurant
  Name, Order Count, and their Rank.
  ● Tables to Use: Restaurants, Orders
