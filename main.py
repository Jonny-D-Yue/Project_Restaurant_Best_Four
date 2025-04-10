import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("KFC Data Management System")
root.geometry("1280x720")

notebook = ttk.Notebook(root)

search_tab = ttk.Frame(notebook)
modify_tab = ttk.Frame(notebook)

notebook.add(search_tab, text="Search")
notebook.add(modify_tab, text="Modify")
notebook.pack(padx=10, pady=10, fill='both', expand=True)

# ---------------------- Search Tab Setup ---------------------- #
frame = tk.Frame(search_tab)
frame.pack(padx=20, pady=20, fill='both', expand=True)

mode_var = tk.StringVar(value="Customer")

customer_labels = ["Name", "Phone", "Address"]
supply_labels = ["Item", "Quantity", "Supplier"]

customer_fields = {}
supply_fields = {}


for i in range(3):
    for j in range(3):
        c_key = f"{customer_labels[i]}_{j}"
        customer_fields[c_key] = {
            "label": tk.Label(frame, text=customer_labels[i]),
            "entry": tk.Entry(frame)
        }
        if not (i == 2 and j == 2):
            s_key = f"{supply_labels[i]}_{j}"
            supply_fields[s_key] = {
                "label": tk.Label(frame, text=supply_labels[i]),
                "entry": tk.Entry(frame)
            }

def show_fields():
    for widget in frame.grid_slaves():
        if 1 <= int(widget.grid_info()["row"]) <= 3:
            widget.grid_forget()

    if mode_var.get() == "Customer":
        for i in range(3):
            for j in range(3):
                key = f"{customer_labels[i]}_{j}"
                label = customer_fields[key]["label"]
                entry = customer_fields[key]["entry"]
                label.grid(row=i+1, column=j*2, padx=5, pady=5, sticky='e')
                entry.grid(row=i+1, column=j*2+1, padx=5, pady=5)
    else:
        for i in range(3):
            for j in range(3):
                if i == 2 and j == 2:
                    continue
                key = f"{supply_labels[i]}_{j}"
                label = supply_fields[key]["label"]
                entry = supply_fields[key]["entry"]
                label.grid(row=i+1, column=j*2, padx=5, pady=5, sticky='e')
                entry.grid(row=i+1, column=j*2+1, padx=5, pady=5)

tk.Radiobutton(frame, text="Customer", variable=mode_var, value="Customer", command=show_fields).grid(row=0, column=1, padx=10, pady=10, sticky='w')
tk.Radiobutton(frame, text="Supply", variable=mode_var, value="Supply", command=show_fields).grid(row=0, column=2, padx=10, pady=10, sticky='w')

tk.Button(frame, text="Search").grid(row=4, column=0, columnspan=6, pady=10)

result_box = tk.Text(frame, height=15, width=160)
result_box.grid(row=5, column=0, columnspan=6, padx=10, pady=20)

show_fields()

# ---------------------- Modify Tab Setup ---------------------- #
modify_notebook = ttk.Notebook(modify_tab)
modify_notebook.pack(padx=10, pady=10, fill='both', expand=True)

# ---------------------- Sub-Tabs in Modify Tab ---------------------- #

# Customers Sub-Tab
customers_tab = ttk.Frame(modify_notebook)
modify_notebook.add(customers_tab, text="CUSTOMERS")
customers_tab_frame = tk.Frame(customers_tab, relief=tk.SOLID, borderwidth=1)
customers_tab_frame.pack(padx=20, pady=20, fill='both', expand=True)

tk.Label(customers_tab_frame, text="First Name").grid(row=0, column=0, padx=5, pady=5, sticky='e')
first_name_entry = tk.Entry(customers_tab_frame)
first_name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(customers_tab_frame, text="Last Name").grid(row=1, column=0, padx=5, pady=5, sticky='e')
last_name_entry = tk.Entry(customers_tab_frame)
last_name_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(customers_tab_frame, text="Phone Number").grid(row=2, column=0, padx=5, pady=5, sticky='e')
phone_number_entry = tk.Entry(customers_tab_frame)
phone_number_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Button(customers_tab_frame, text="Save").grid(row=3, column=0, columnspan=2, pady=10)

# Employees Sub-Tab
employees_tab = ttk.Frame(modify_notebook)
modify_notebook.add(employees_tab, text="EMPLOYEES")
employees_tab_frame = tk.Frame(employees_tab, relief=tk.SOLID, borderwidth=1)
employees_tab_frame.pack(padx=20, pady=20, fill='both', expand=True)

tk.Label(employees_tab_frame, text="SIN").grid(row=0, column=0, padx=5, pady=5, sticky='e')
sin_entry = tk.Entry(employees_tab_frame)
sin_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(employees_tab_frame, text="First Name").grid(row=1, column=0, padx=5, pady=5, sticky='e')
first_name_entry = tk.Entry(employees_tab_frame)
first_name_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(employees_tab_frame, text="Last Name").grid(row=2, column=0, padx=5, pady=5, sticky='e')
last_name_entry = tk.Entry(employees_tab_frame)
last_name_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(employees_tab_frame, text="Job Title").grid(row=3, column=0, padx=5, pady=5, sticky='e')
job_title_entry = tk.Entry(employees_tab_frame)
job_title_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(employees_tab_frame, text="Salary").grid(row=4, column=0, padx=5, pady=5, sticky='e')
salary_entry = tk.Entry(employees_tab_frame)
salary_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Label(employees_tab_frame, text="Hire Date").grid(row=5, column=0, padx=5, pady=5, sticky='e')
hire_date_entry = tk.Entry(employees_tab_frame)
hire_date_entry.grid(row=5, column=1, padx=5, pady=5)

tk.Label(employees_tab_frame, text="Phone Number").grid(row=6, column=0, padx=5, pady=5, sticky='e')
phone_number_entry = tk.Entry(employees_tab_frame)
phone_number_entry.grid(row=6, column=1, padx=5, pady=5)

tk.Label(employees_tab_frame, text="Address").grid(row=7, column=0, padx=5, pady=5, sticky='e')
address_entry = tk.Entry(employees_tab_frame)
address_entry.grid(row=7, column=1, padx=5, pady=5)

tk.Label(employees_tab_frame, text="Supervisor ID").grid(row=8, column=0, padx=5, pady=5, sticky='e')
supervisor_id_entry = tk.Entry(employees_tab_frame)
supervisor_id_entry.grid(row=8, column=1, padx=5, pady=5)

tk.Label(employees_tab_frame, text="DOB").grid(row=9, column=0, padx=5, pady=5, sticky='e')
dob_entry = tk.Entry(employees_tab_frame)
dob_entry.grid(row=9, column=1, padx=5, pady=5)

tk.Button(employees_tab_frame, text="Save").grid(row=10, column=0, columnspan=2, pady=10)

# Menu Items Sub-Tab
menu_items_tab = ttk.Frame(modify_notebook)
modify_notebook.add(menu_items_tab, text="MENU_ITEMS")
menu_items_tab_frame = tk.Frame(menu_items_tab, relief=tk.SOLID, borderwidth=1)
menu_items_tab_frame.pack(padx=20, pady=20, fill='both', expand=True)

tk.Label(menu_items_tab_frame, text="Name").grid(row=0, column=0, padx=5, pady=5, sticky='e')
name_entry = tk.Entry(menu_items_tab_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(menu_items_tab_frame, text="Description").grid(row=1, column=0, padx=5, pady=5, sticky='e')
description_entry = tk.Entry(menu_items_tab_frame)
description_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(menu_items_tab_frame, text="Category").grid(row=2, column=0, padx=5, pady=5, sticky='e')
category_entry = tk.Entry(menu_items_tab_frame)
category_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(menu_items_tab_frame, text="Price").grid(row=3, column=0, padx=5, pady=5, sticky='e')
price_entry = tk.Entry(menu_items_tab_frame)
price_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Button(menu_items_tab_frame, text="Save").grid(row=4, column=0, columnspan=2, pady=10)

# Orders Sub-Tab
orders_tab = ttk.Frame(modify_notebook)
modify_notebook.add(orders_tab, text="ORDERS")
orders_tab_frame = tk.Frame(orders_tab, relief=tk.SOLID, borderwidth=1)
orders_tab_frame.pack(padx=20, pady=20, fill='both', expand=True)

tk.Label(orders_tab_frame, text="Employee ID").grid(row=0, column=0, padx=5, pady=5, sticky='e')
employee_id_entry = tk.Entry(orders_tab_frame)
employee_id_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(orders_tab_frame, text="Customer ID").grid(row=1, column=0, padx=5, pady=5, sticky='e')
customer_id_entry = tk.Entry(orders_tab_frame)
customer_id_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(orders_tab_frame, text="Order Date").grid(row=2, column=0, padx=5, pady=5, sticky='e')
order_date_entry = tk.Entry(orders_tab_frame)
order_date_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(orders_tab_frame, text="Order Time").grid(row=3, column=0, padx=5, pady=5, sticky='e')
order_time_entry = tk.Entry(orders_tab_frame)
order_time_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(orders_tab_frame, text="Status").grid(row=4, column=0, padx=5, pady=5, sticky='e')
status_entry = tk.Entry(orders_tab_frame)
status_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Label(orders_tab_frame, text="Total Amount").grid(row=5, column=0, padx=5, pady=5, sticky='e')
total_amount_entry = tk.Entry(orders_tab_frame)
total_amount_entry.grid(row=5, column=1, padx=5, pady=5)

tk.Button(orders_tab_frame, text="Save").grid(row=6, column=0, columnspan=2, pady=10)

# Order Details Sub-Tab
order_details_tab = ttk.Frame(modify_notebook)
modify_notebook.add(order_details_tab, text="ORDER_DETAILS")
order_details_tab_frame = tk.Frame(order_details_tab, relief=tk.SOLID, borderwidth=1)
order_details_tab_frame.pack(padx=20, pady=20, fill='both', expand=True)

tk.Label(order_details_tab_frame, text="Order ID").grid(row=0, column=0, padx=5, pady=5, sticky='e')
order_id_entry = tk.Entry(order_details_tab_frame)
order_id_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(order_details_tab_frame, text="Item ID").grid(row=1, column=0, padx=5, pady=5, sticky='e')
item_id_entry = tk.Entry(order_details_tab_frame)
item_id_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(order_details_tab_frame, text="Quantity").grid(row=2, column=0, padx=5, pady=5, sticky='e')
quantity_entry = tk.Entry(order_details_tab_frame)
quantity_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(order_details_tab_frame, text="Special Instructions").grid(row=3, column=0, padx=5, pady=5, sticky='e')
special_instructions_entry = tk.Entry(order_details_tab_frame)
special_instructions_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(order_details_tab_frame, text="Status").grid(row=4, column=0, padx=5, pady=5, sticky='e')
status_entry = tk.Entry(order_details_tab_frame)
status_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Button(order_details_tab_frame, text="Save").grid(row=5, column=0, columnspan=2, pady=10)

# Payments Sub-Tab
payments_tab = ttk.Frame(modify_notebook)
modify_notebook.add(payments_tab, text="PAYMENTS")
payments_tab_frame = tk.Frame(payments_tab, relief=tk.SOLID, borderwidth=1)
payments_tab_frame.pack(padx=20, pady=20, fill='both', expand=True)

tk.Label(payments_tab_frame, text="Order ID").grid(row=0, column=0, padx=5, pady=5, sticky='e')
order_id_entry = tk.Entry(payments_tab_frame)
order_id_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(payments_tab_frame, text="Employee ID").grid(row=1, column=0, padx=5, pady=5, sticky='e')
employee_id_entry = tk.Entry(payments_tab_frame)
employee_id_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(payments_tab_frame, text="Payment Date").grid(row=2, column=0, padx=5, pady=5, sticky='e')
payment_date_entry = tk.Entry(payments_tab_frame)
payment_date_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(payments_tab_frame, text="Payment Time").grid(row=3, column=0, padx=5, pady=5, sticky='e')
payment_time_entry = tk.Entry(payments_tab_frame)
payment_time_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(payments_tab_frame, text="Amount").grid(row=4, column=0, padx=5, pady=5, sticky='e')
amount_entry = tk.Entry(payments_tab_frame)
amount_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Label(payments_tab_frame, text="Payment Method").grid(row=5, column=0, padx=5, pady=5, sticky='e')
payment_method_entry = tk.Entry(payments_tab_frame)
payment_method_entry.grid(row=5, column=1, padx=5, pady=5)

tk.Label(payments_tab_frame, text="Transaction Status").grid(row=6, column=0, padx=5, pady=5, sticky='e')
transaction_status_entry = tk.Entry(payments_tab_frame)
transaction_status_entry.grid(row=6, column=1, padx=5, pady=5)

tk.Button(payments_tab_frame, text="Save").grid(row=7, column=0, columnspan=2, pady=10)

# Suppliers Sub-Tab
suppliers_tab = ttk.Frame(modify_notebook)
modify_notebook.add(suppliers_tab, text="SUPPLIERS")
suppliers_tab_frame = tk.Frame(suppliers_tab, relief=tk.SOLID, borderwidth=1)
suppliers_tab_frame.pack(padx=20, pady=20, fill='both', expand=True)

tk.Label(suppliers_tab_frame, text="Name").grid(row=0, column=0, padx=5, pady=5, sticky='e')
name_entry = tk.Entry(suppliers_tab_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(suppliers_tab_frame, text="Contact Person").grid(row=1, column=0, padx=5, pady=5, sticky='e')
contact_person_entry = tk.Entry(suppliers_tab_frame)
contact_person_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(suppliers_tab_frame, text="Phone Number").grid(row=2, column=0, padx=5, pady=5, sticky='e')
phone_number_entry = tk.Entry(suppliers_tab_frame)
phone_number_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(suppliers_tab_frame, text="Email").grid(row=3, column=0, padx=5, pady=5, sticky='e')
email_entry = tk.Entry(suppliers_tab_frame)
email_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(suppliers_tab_frame, text="Address").grid(row=4, column=0, padx=5, pady=5, sticky='e')
address_entry = tk.Entry(suppliers_tab_frame)
address_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Label(suppliers_tab_frame, text="Payment Terms").grid(row=5, column=0, padx=5, pady=5, sticky='e')
payment_terms_entry = tk.Entry(suppliers_tab_frame)
payment_terms_entry.grid(row=5, column=1, padx=5, pady=5)

tk.Button(suppliers_tab_frame, text="Save").grid(row=6, column=0, columnspan=2, pady=10)

# Inventory Sub-Tab
inventory_tab = ttk.Frame(modify_notebook)
modify_notebook.add(inventory_tab, text="INVENTORY")
inventory_tab_frame = tk.Frame(inventory_tab, relief=tk.SOLID, borderwidth=1)
inventory_tab_frame.pack(padx=20, pady=20, fill='both', expand=True)

tk.Label(inventory_tab_frame, text="Inventory ID").grid(row=0, column=0, padx=5, pady=5, sticky='e')
inventory_id_entry = tk.Entry(inventory_tab_frame)
inventory_id_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(inventory_tab_frame, text="Supplier ID").grid(row=1, column=0, padx=5, pady=5, sticky='e')
supplier_id_entry = tk.Entry(inventory_tab_frame)
supplier_id_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(inventory_tab_frame, text="Name").grid(row=2, column=0, padx=5, pady=5, sticky='e')
name_entry = tk.Entry(inventory_tab_frame)
name_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(inventory_tab_frame, text="Category").grid(row=3, column=0, padx=5, pady=5, sticky='e')
category_entry = tk.Entry(inventory_tab_frame)
category_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(inventory_tab_frame, text="Quantity").grid(row=4, column=0, padx=5, pady=5, sticky='e')
quantity_entry = tk.Entry(inventory_tab_frame)
quantity_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Label(inventory_tab_frame, text="Unit").grid(row=5, column=0, padx=5, pady=5, sticky='e')
unit_entry = tk.Entry(inventory_tab_frame)
unit_entry.grid(row=5, column=1, padx=5, pady=5)

tk.Label(inventory_tab_frame, text="Reorder Level").grid(row=6, column=0, padx=5, pady=5, sticky='e')
reorder_level_entry = tk.Entry(inventory_tab_frame)
reorder_level_entry.grid(row=6, column=1, padx=5, pady=5)

tk.Label(inventory_tab_frame, text="Unit Cost").grid(row=7, column=0, padx=5, pady=5, sticky='e')
unit_cost_entry = tk.Entry(inventory_tab_frame)
unit_cost_entry.grid(row=7, column=1, padx=5, pady=5)

tk.Button(inventory_tab_frame, text="Save").grid(row=8, column=0, columnspan=2, pady=10)

# Purchases Sub-Tab
purchases_tab = ttk.Frame(modify_notebook)
modify_notebook.add(purchases_tab, text="PURCHASES")
purchases_tab_frame = tk.Frame(purchases_tab, relief=tk.SOLID, borderwidth=1)
purchases_tab_frame.pack(padx=20, pady=20, fill='both', expand=True)

tk.Label(purchases_tab_frame, text="Supplier ID").grid(row=0, column=0, padx=5, pady=5, sticky='e')
supplier_id_entry = tk.Entry(purchases_tab_frame)
supplier_id_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(purchases_tab_frame, text="Employee ID").grid(row=1, column=0, padx=5, pady=5, sticky='e')
employee_id_entry = tk.Entry(purchases_tab_frame)
employee_id_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(purchases_tab_frame, text="Purchase Date").grid(row=2, column=0, padx=5, pady=5, sticky='e')
purchase_date_entry = tk.Entry(purchases_tab_frame)
purchase_date_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(purchases_tab_frame, text="Total Amount").grid(row=3, column=0, padx=5, pady=5, sticky='e')
total_amount_entry = tk.Entry(purchases_tab_frame)
total_amount_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Button(purchases_tab_frame, text="Save").grid(row=4, column=0, columnspan=2, pady=10)

# Purchase Details Sub-Tab
purchase_details_tab = ttk.Frame(modify_notebook)
modify_notebook.add(purchase_details_tab, text="PURCHASE_DETAILS")
purchase_details_tab_frame = tk.Frame(purchase_details_tab, relief=tk.SOLID, borderwidth=1)
purchase_details_tab_frame.pack(padx=20, pady=20, fill='both', expand=True)

tk.Label(purchase_details_tab_frame, text="Purchase ID").grid(row=0, column=0, padx=5, pady=5, sticky='e')
purchase_id_entry = tk.Entry(purchase_details_tab_frame)
purchase_id_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(purchase_details_tab_frame, text="Inventory ID").grid(row=1, column=0, padx=5, pady=5, sticky='e')
inventory_id_entry = tk.Entry(purchase_details_tab_frame)
inventory_id_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(purchase_details_tab_frame, text="Quantity").grid(row=2, column=0, padx=5, pady=5, sticky='e')
quantity_entry = tk.Entry(purchase_details_tab_frame)
quantity_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(purchase_details_tab_frame, text="Unit Price").grid(row=3, column=0, padx=5, pady=5, sticky='e')
unit_price_entry = tk.Entry(purchase_details_tab_frame)
unit_price_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(purchase_details_tab_frame, text="Total Price").grid(row=4, column=0, padx=5, pady=5, sticky='e')
total_price_entry = tk.Entry(purchase_details_tab_frame)
total_price_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Button(purchase_details_tab_frame, text="Save").grid(row=5, column=0, columnspan=2, pady=10)

# Start the main loop
root.mainloop()