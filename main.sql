-- Create tables
CREATE TABLE Employee (
    eno INT PRIMARY KEY,
    ename VARCHAR(50),
    deptname VARCHAR(50),
    salary DECIMAL(10, 2) CHECK (salary > 0)
);

CREATE TABLE Project (
    pno INT PRIMARY KEY,
    name VARCHAR(50),
    budget DECIMAL(10, 2)
);

CREATE TABLE Works_On (
    eno INT,
    pno INT,
    PRIMARY KEY (eno, pno),
    FOREIGN KEY (eno) REFERENCES Employee(eno),
    FOREIGN KEY (pno) REFERENCES Project(pno)
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);

CREATE TABLE Product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    rate DECIMAL(10, 2),
    supplier_id INT,
    FOREIGN KEY (supplier_id) REFERENCES Supplier(supplier_id)
);

CREATE TABLE Supplier (
    supplier_id INT PRIMARY KEY,
    supplier_name VARCHAR(50),
    city VARCHAR(50)
);

CREATE TABLE Customer (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50)
);

-- Insert sample data
INSERT INTO Employee (eno, ename, deptname, salary) VALUES
(1, 'John', 'HR', 60000),
(2, 'Alice', 'Finance', 55000),
(3, 'Bob', 'IT', 65000),
(4, 'Ramesh', 'Marketing', 70000),
(5, 'Emily', 'HR', 50000);

INSERT INTO Project (pno, name, budget) VALUES
(101, 'Project A', 40000),
(102, 'Project B', 60000),
(103, 'Project C', 35000);

INSERT INTO Works_On (eno, pno) VALUES
(1, 101),
(2, 101),
(3, 102),
(4, 102),
(5, 103),
(1, 102),
(4, 103);

INSERT INTO Orders (order_id, customer_id, product_id, quantity) VALUES
(1, 101, 1, 5),
(2, 102, 2, 3),
(3, 103, 1, 2),
(4, 101, 3, 4),
(5, 104, 2, 6);

INSERT INTO Product (product_id, product_name, rate, supplier_id) VALUES
(1, 'Product A', 10.99, 201),
(2, 'Product B', 20.50, 202),
(3, 'Product C', 15.75, 203);

INSERT INTO Supplier (supplier_id, supplier_name, city) VALUES
(201, 'Supplier X', 'Pune'),
(202, 'Supplier Y', 'Mumbai'),
(203, 'Supplier Z', 'Delhi');

INSERT INTO Customer (customer_id, customer_name) VALUES
(101, 'Customer A'),
(102, 'Customer B'),
(103, 'Customer C'),
(104, 'Customer D');

-- Queries
-- 1. List the name of employee and department having salary > 50000
SELECT ename, deptname
FROM Employee
WHERE salary > 50000;

-- 2. List names of all employees who work with 'Ramesh' on the same project
SELECT DISTINCT e1.ename
FROM Employee e1
JOIN Works_On w1 ON e1.eno = w1.eno
JOIN Works_On w2 ON w1.pno = w2.pno
JOIN Employee e2 ON w2.eno = e2.eno
WHERE e2.ename = 'Ramesh';

-- 3. Find the names of employees who are working on projects with a budget greater than 30000
SELECT DISTINCT e.ename
FROM Employee e
JOIN Works_On w ON e.eno = w.eno
JOIN Project p ON w.pno = p.pno
WHERE p.budget > 30000;

-- 4. Display the total quantity of each product sold by 'Mr. Khabia'
SELECT p.product_name, SUM(o.quantity) AS total_quantity
FROM Orders o
JOIN Product p ON o.product_id = p.product_id
JOIN Customer c ON o.customer_id = c.customer_id
WHERE c.customer_name = 'Mr. Khabia'
GROUP BY p.product_name;

-- 5. Decrement the rate of all products supplied by wholesalers from 'Pune' city by 5%
UPDATE Product
SET rate = rate * 0.95
WHERE supplier_id IN (SELECT supplier_id FROM Supplier WHERE city = 'Pune');
