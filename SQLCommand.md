CREATE DATABASE
kfood_pos;
USE kfood_pos;


CREATE TABLE CUSTOMERS (
customer_id INT AUTO_INCREMENT PRIMARY KEY,
first_name VARCHAR(30) NOT NULL,
last_name VARCHAR(30) NOT NULL,
phone_number VARCHAR(14) NOT NULL,
CHECK (phone_number REGEXP '^\\([0-9]{3}\\)[0-9]{3}-[0-9]{4}$')
) AUTO_INCREMENT = 300001;


CREATE TABLE EMPLOYEES (
employee_id INT AUTO_INCREMENT PRIMARY KEY,
sin VARCHAR(11) NOT NULL UNIQUE,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
job_title VARCHAR(50) NOT NULL,
dob DATE NOT NULL,
salary DECIMAL(10, 2) NOT NULL,
hire_date DATE NOT NULL,
phone_number VARCHAR(14) NOT NULL,
address VARCHAR(100) NOT NULL,
supervisor_id INT,
CHECK (phone_number REGEXP '^\\([0-9]{3}\\)[0-9]{3}-[0-9]{4}$'),
CONSTRAINT fk_supervisor FOREIGN KEY (supervisor_id) REFERENCES EMPLOYEES(employee_id) ON DELETE SET NULL
) AUTO_INCREMENT = 101;


CREATE TABLE ORDERS (
order_id INT AUTO_INCREMENT PRIMARY KEY,
employee_id INT NOT NULL,
customer_id INT,
order_date DATE NOT NULL,
order_time TIME NOT NULL,
status ENUM('Pending', 'In Preparation', 'Served', 'Completed') NOT NULL DEFAULT 'Pending',
total_amount DECIMAL(6, 2) NOT NULL DEFAULT 0.00,
CONSTRAINT fk_order_employee FOREIGN KEY (employee_id) REFERENCES EMPLOYEES(employee_id) ON DELETE RESTRICT,
CONSTRAINT fk_order_customer FOREIGN KEY (customer_id) REFERENCES CUSTOMERS(customer_id) ON DELETE SET NULL
) AUTO_INCREMENT = 20250001;


CREATE TABLE MENU_ITEMS (
item_id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100) NOT NULL,
description TEXT,
category VARCHAR(25) NOT NULL,
price DECIMAL(5, 2) NOT NULL
) AUTO_INCREMENT = 9001;


CREATE TABLE ORDER_DETAILS (
order_detail_id INT AUTO_INCREMENT PRIMARY KEY,
order_id INT NOT NULL,
item_id INT NOT NULL,
quantity INT NOT NULL,
special_instructions TEXT,
status ENUM('Pending', 'Cooking', 'Ready', 'Served') NOT NULL DEFAULT 'Pending',
CONSTRAINT fk_orderdetail_order FOREIGN KEY (order_id) REFERENCES ORDERS(order_id) ON DELETE CASCADE,
CONSTRAINT fk_orderdetail_item FOREIGN KEY (item_id) REFERENCES MENU_ITEMS(item_id) ON DELETE RESTRICT
);


CREATE TABLE PAYMENTS (
payment_id INT AUTO_INCREMENT PRIMARY KEY,
order_id INT NOT NULL,
employee_id INT NOT NULL,
payment_date DATE NOT NULL,
payment_time TIME NOT NULL,
amount DECIMAL(10, 2) NOT NULL,
payment_method ENUM('Cash', 'Credit Card', 'Debit Card', 'Mobile Payment') NOT NULL,
transaction_status ENUM('Completed', 'Pending', 'Failed') NOT NULL DEFAULT 'Completed',
CONSTRAINT fk_payment_order FOREIGN KEY (order_id) REFERENCES ORDERS(order_id) ON DELETE RESTRICT,
CONSTRAINT fk_payment_employee FOREIGN KEY (employee_id) REFERENCES EMPLOYEES(employee_id) ON DELETE RESTRICT
);

CREATE TABLE SUPPLIERS (
supplier_id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100) NOT NULL,
contact_person VARCHAR(100) NOT NULL,
phone_number VARCHAR(14) NOT NULL,
email VARCHAR(100) NOT NULL UNIQUE,
address VARCHAR(255) NOT NULL,
payment_terms VARCHAR(50) NOT NULL,
CHECK (phone_number REGEXP '^\\([0-9]{3}\\)[0-9]{3}-[0-9]{4}$')
)AUTO_INCREMENT = 601;


CREATE TABLE INVENTORY (
inventory_id INT AUTO_INCREMENT PRIMARY KEY,
supplier_id INT,
name VARCHAR(100) NOT NULL,
category VARCHAR(50) NOT NULL,
quantity DECIMAL(10, 2) NOT NULL DEFAULT 0,
unit VARCHAR(20) NOT NULL,
reorder_level DECIMAL(10, 2) NOT NULL,
unit_cost DECIMAL(10, 2) NOT NULL,
CONSTRAINT fk_inventory_supplier FOREIGN KEY (supplier_id) REFERENCES SUPPLIERS(supplier_id) ON DELETE SET NULL
) AUTO_INCREMENT = 6001;


CREATE TABLE PURCHASES (
purchase_id INT AUTO_INCREMENT PRIMARY KEY,
supplier_id INT NOT NULL,
employee_id INT NOT NULL,
purchase_date DATE NOT NULL,
total_amount DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
CONSTRAINT fk_purchase_supplier FOREIGN KEY (supplier_id) REFERENCES SUPPLIERS(supplier_id) ON DELETE RESTRICT,
CONSTRAINT fk_purchase_employee FOREIGN KEY (employee_id) REFERENCES EMPLOYEES(employee_id) ON DELETE RESTRICT
) AUTO_INCREMENT = 20001;


CREATE TABLE PURCHASE_DETAILS (
purchase_detail_id INT AUTO_INCREMENT PRIMARY KEY,
purchase_id INT NOT NULL,
inventory_id INT NOT NULL,
quantity DECIMAL(5, 2) NOT NULL,
unit_price DECIMAL(6, 2) NOT NULL,
total_price DECIMAL(10, 2) NOT NULL,
CONSTRAINT fk_purchasedetail_purchase FOREIGN KEY (purchase_id) REFERENCES PURCHASES(purchase_id) ON DELETE CASCADE,
CONSTRAINT fk_purchasedetail_inventory FOREIGN KEY (inventory_id) REFERENCES INVENTORY(inventory_id) ON DELETE RESTRICT
);
