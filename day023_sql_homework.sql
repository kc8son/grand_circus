/**********************************************************************\
 *
 *  Date Written: 04/20/2023        By: Joseph P. Merten
 *  This is the SQL homework assignment for day 23
 *
\**********************************************************************/
-- Select all the records from the customers table.
SELECT * FROM customers;

-- Get distinct countries from the customers table.
SELECT DISTINCT country FROM customers;

-- Get all the records from the table customers where the customer_id starts with “BL”.
SELECT * FROM customers WHERE customer_id LIKE 'BL%';

-- Get the first 100 records of the orders table.
SELECT * FROM orders LIMIT 100;

-- Get all customers that live in the postal codes 1010, 3012, 12209, and 05023.
SELECT * FROM customers WHERE postal_code in ('1010', '3012', '12209', '05023');

-- Get all orders where the ShipRegion is not equal to NULL.
SELECT * FROM orders WHERE ship_region IS NOT NULL;

-- Get all customers ordered by the country, then by the city.
SELECT * FROM customers ORDER BY country, city;

-- Add a new customer to the customers table. You can use whatever values/
INSERT INTO customers VALUES ('JMENT', 'JM Enterprises', 'Joe Merten', 'Owner', '123 Main Streeet', 'Minneapoils', 'MN', '55435', 'USA', '(612)555-1122', '(612)555-2211');
SELECT * FROM customers WHERE country = 'USA' ORDER BY region, city;


-- Update all ship_region to the value 'EuroZone' in the orders table, where the ship_country is 'France'.
select * from orders    -- Initially these are all NULL
--  UPDATE orders SET ship_region = 'EuroZone'
WHERE ship_country = 'France'

-- Delete all rows from order_details that have a quantity of 1.
SELECT *
--  DELETE  -- 17 rows
FROM order_details WHERE quantity = 1;

-- Calculate the average, max, and min of the quantity in the order_details table.
SELECT
    AVG(quantity) AS avg_qty,
    MAX(quantity) AS max_qty,
    MIN(quantity) as max_qty
FROM order_details

-- Calculate the average, max, and min of the quantity in the order_details table, grouped by the order_id.
SELECT
    order_id,
    AVG(quantity) AS avg_qty,
    MAX(quantity) AS max_qty,
    MIN(quantity) as max_qty
FROM order_details
GROUP BY order_id;

-- Find the customer_id that placed order 10290 (orders table)
SELECT customer_id FROM orders WHERE order_id = 10290;

-- Do an inner join, left join, right join on orders and customers tables.  (These are three separate queries, one for each type of join.)
SELECT *
FROM orders o
    JOIN customers c    --   default is INNER
        ON o.customer_id = c.customer_id;

SELECT *
FROM orders o
    LEFT JOIN customers c    --   default is INNER
        ON o.customer_id = c.customer_id
ORDER BY c.customer_id;

SELECT *
FROM orders o
    RIGHT JOIN customers c    --   default is INNER
        ON o.customer_id = c.customer_id
ORDER BY c.customer_id;

-- Use a join to get the ship_city and ship_country of all the orders which are associated with an employee who is in London.
SELECT o.order_id, o.ship_city, o.ship_country
FROM orders o
    JOIN employees e ON o.employee_id = e.employee_id
WHERE e.city = 'London';

-- Use a join to get the ship_name of all orders that include a discontinued product. (See orders, order_details, and products. 1 means discontinued.)
SELECT o.ship_name
FROM products p
    JOIN order_details od
        ON p.product_id = od.product_id
    JOIN orders o
        ON od.order_id = o.order_id
WHERE p.discontinued = 1;

-- Get first names of all employees who report to no one.
SELECT *
FROM employees
WHERE reports_to IS NULL;

-- Get first names of all employees who report to 'Andrew'.
SELECT first_name
FROM employees
WHERE reports_to IN
    (SELECT employee_id FROM employees WHERE first_name = 'Andrew');

----- OR -----

SELECT e1.first_name
FROM employees e1
    JOIN employees e2
        ON e1.reports_to = e2.employee_id
WHERE e2.first_name = 'Andrew'

