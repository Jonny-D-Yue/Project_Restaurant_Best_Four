import tkinter as tk
from tkinter import ttk

# Root window
root = tk.Tk()
root.title("KFC Data Management System")
root.geometry("1280x720")

# Tabs
notebook = ttk.Notebook(root)
search_tab = ttk.Frame(notebook)
modify_tab = ttk.Frame(notebook)
notebook.add(search_tab, text="search")
notebook.add(modify_tab, text="modify")
notebook.pack(pady=10, fill='x')

# Frame inside the tab
frame = tk.Frame(search_tab, relief=tk.SOLID, borderwidth=1)
frame.pack(padx=20, pady=20, fill='both', expand=True)

mode_var = tk.StringVar(value="Customer")

# Labels per row
customer_labels = ["name", "phone", "address"]
supply_labels = ["item", "quantity", "supplier"]

# Store widgets
customer_fields = {}
supply_fields = {}

# Create 3x3 structure
for i in range(3):  # rows
    for j in range(3):  # columns
        # Customer setup
        c_key = f"{customer_labels[i]}_{j}"
        customer_fields[c_key] = {
            "label": tk.Label(frame, text=customer_labels[i]),
            "entry": tk.Entry(frame)
        }
        # Supply setup
        if not (i == 2 and j == 2):  # skip bottom-right
            s_key = f"{supply_labels[i]}_{j}"
            supply_fields[s_key] = {
                "label": tk.Label(frame, text=supply_labels[i]),
                "entry": tk.Entry(frame)
            }

# Show fields
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

# Radio buttons
tk.Radiobutton(frame, text="Customer", variable=mode_var, value="Customer", command=show_fields)\
    .grid(row=0, column=1, padx=10, pady=10, sticky='w')
tk.Radiobutton(frame, text="Supply", variable=mode_var, value="Supply", command=show_fields)\
    .grid(row=0, column=2, padx=10, pady=10, sticky='w')

# Search button
tk.Button(frame, text="search").grid(row=4, column=0, columnspan=6, pady=10)

# Result Box
result_box = tk.Text(frame, height=15, width=160)
result_box.grid(row=5, column=0, columnspan=6, padx=10, pady=20)

# Initialize
show_fields()
root.mainloop()