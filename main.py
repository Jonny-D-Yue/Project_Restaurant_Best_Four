import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("KFC Data Management System")
root.geometry("1280x720")

# ---------------------- MENU BAR ---------------------- #
notebook = ttk.Notebook(root)
search_tab = ttk.Frame(notebook)
modify_tab = ttk.Frame(notebook)
notebook.add(search_tab, text="search")
notebook.add(modify_tab, text="modify")
notebook.pack(pady=10, fill='both', expand=True)

# ---------------------- SEARCH TAB ---------------------- #
frame = tk.Frame(search_tab, relief=tk.SOLID, borderwidth=1)
frame.pack(padx=20, pady=20, fill='both', expand=True)

mode_var = tk.StringVar(value="Customer")

customer_labels = ["name", "phone", "address"]
supply_labels = ["item", "quantity", "supplier"]

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

tk.Radiobutton(frame, text="Customer", variable=mode_var, value="Customer", command=show_fields)\
    .grid(row=0, column=1, padx=10, pady=10, sticky='w')
tk.Radiobutton(frame, text="Supply", variable=mode_var, value="Supply", command=show_fields)\
    .grid(row=0, column=2, padx=10, pady=10, sticky='w')

tk.Button(frame, text="search").grid(row=4, column=0, columnspan=6, pady=10)

result_box = tk.Text(frame, height=15, width=160)
result_box.grid(row=5, column=0, columnspan=6, padx=10, pady=20)

# ---------------------- MODIFY TAB ---------------------- #
modify_frame = tk.Frame(modify_tab, relief=tk.SOLID, borderwidth=1)
modify_frame.pack(padx=20, pady=20, fill='both', expand=True)

tk.Label(modify_frame, text="inventory_id").grid(row=0, column=0, padx=5, pady=5, sticky='e')
inventory_id_entry = tk.Entry(modify_frame)
inventory_id_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(modify_frame, text="supplier_id").grid(row=1, column=0, padx=5, pady=5, sticky='e')
supplier_id_entry = tk.Entry(modify_frame)
supplier_id_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(modify_frame, text="name").grid(row=2, column=0, padx=5, pady=5, sticky='e')
name_entry = tk.Entry(modify_frame)
name_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(modify_frame, text="category").grid(row=3, column=0, padx=5, pady=5, sticky='e')
category_entry = tk.Entry(modify_frame)
category_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(modify_frame, text="quantity").grid(row=4, column=0, padx=5, pady=5, sticky='e')
quantity_entry = tk.Entry(modify_frame)
quantity_entry.grid(row=4, column=1, padx=5, pady=5)

tk.Label(modify_frame, text="unit").grid(row=5, column=0, padx=5, pady=5, sticky='e')
unit_entry = tk.Entry(modify_frame)
unit_entry.grid(row=5, column=1, padx=5, pady=5)

tk.Label(modify_frame, text="reorder_level").grid(row=6, column=0, padx=5, pady=5, sticky='e')
reorder_level_entry = tk.Entry(modify_frame)
reorder_level_entry.grid(row=6, column=1, padx=5, pady=5)

tk.Label(modify_frame, text="unit_cost").grid(row=7, column=0, padx=5, pady=5, sticky='e')
unit_cost_entry = tk.Entry(modify_frame)
unit_cost_entry.grid(row=7, column=1, padx=5, pady=5)

def save_inventory():
    data = {
        "inventory_id": inventory_id_entry.get(),
        "supplier_id": supplier_id_entry.get(),
        "name": name_entry.get(),
        "category": category_entry.get(),
        "quantity": quantity_entry.get(),
        "unit": unit_entry.get(),
        "reorder_level": reorder_level_entry.get(),
        "unit_cost": unit_cost_entry.get()
    }
    print("Saving inventory:", data)

tk.Button(modify_frame, text="Save", command=save_inventory)\
    .grid(row=8, column=0, columnspan=2, pady=10)

show_fields()
root.mainloop()