import tkinter as tk
from tkinter import ttk, messagebox
from db import connect_db
from db import get_columns_for_table
from db import get_table_names
from db import get_foreign_key_database
from modify import load_data
from modify import add_record
from modify import update_record
from modify import delete_record
from modify import clear_fields
from search import search_record
from search import clear_fields_search
from save import export_to_csv

# def Search_Form(table_name, schema_name, search_tab):
    # form_frame = tk.LabelFrame(search_tab, text=f"{table_name} Info", padx=8, pady=4)
    # form_frame.pack(fill="x", padx=8, pady=4)

    # # self.columns = get_columns_for_table(table_name, schema_name)
    # cursor.execute(f"DESCRIBE {table_name}")
    # columns = cursor.fetchall()
    # col_names = [col[0] for col in columns]
    # # self.primary_key = columns[0][0]

    # entry_vars = {}
    # for idx, col in enumerate(col_names):
    #     row_index = 0
    #     if idx >= 10:
    #         idx = idx - 10
    #         row_index = 1
    #     label = tk.Label(form_frame, text=col + ":")
    #     label.grid(row=row_index, column=0+idx*2, sticky="e", padx=4, pady=2)

    #     var = tk.StringVar()
    #     entry = tk.Entry(form_frame, textvariable=var, width=16)
    #     entry.grid(row=row_index, column=1+idx*2, padx=4, pady=2)
    #     entry_vars[col] = var

    #     # self.entries[col] = entry

    #     # self.tree = ttk.Treeview(self.tab)
    #     # self.tree.pack(fill="both", expand=True, padx=8, pady=8)

    # all_entry_vars[table_name] = entry_vars

################################
def Search_Form(event=None):
    conn = connect_db()
    cursor = conn.cursor()
    
    for widget in search_area.winfo_children():
        widget.destroy()

    table = selected_table.get()

    cursor.execute(f"DESCRIBE {table}")
    global columns
    columns = [col[0] for col in cursor.fetchall()]

    # form_frame = tk.LabelFrame(search_area, text=f"{table} Info", padx=8, pady=8)
    # form_frame.pack(fill="x", padx=8, pady=8)

    global search_entries
    search_entries = {}
    for idx, col in enumerate(columns):
        row_index = 0
        if idx >= 7:
            idx = idx - 7
            row_index = 1
        tk.Label(search_area, text=col).grid(row=row_index*2, column=idx, padx=5, pady=5)
        ent = tk.Entry(search_area, width=30)
        ent.grid(row=row_index*2+1, column=idx, padx=5, pady=5)
        search_entries[col] = ent

    cursor.close()
    conn.close()
################################
class Modify:
    def __init__(self, table_name, schema_name, modify_notebook):
        conn = connect_db()
        cursor = conn.cursor()

        self.table_name = table_name
        # self.entries = {}
        self.tab = ttk.Frame(modify_notebook)
        modify_notebook.add(self.tab, text=table_name)

        form_frame = tk.LabelFrame(self.tab, text=f"{table_name} Info", padx=8, pady=8)
        form_frame.pack(fill="x", padx=8, pady=8)

        # self.columns = get_columns_for_table(table_name, schema_name)
        cursor.execute(f"DESCRIBE {table_name}")
        columns = cursor.fetchall()
        self.col_names = [col[0] for col in columns]
        self.primary_key = columns[0][0]

        self.entry_vars = {}
        for idx, col in enumerate(self.col_names):
            if col == self.primary_key:
              continue
            label = tk.Label(form_frame, text=col + ":")
            label.grid(row=idx, column=0, sticky="e", padx=4, pady=2)

            var = tk.StringVar()
            entry = tk.Entry(form_frame, textvariable=var, width=30)
            entry.grid(row=idx, column=1, padx=4, pady=2)
            self.entry_vars[col] = var

            # self.entries[col] = entry

        self.tree = ttk.Treeview(self.tab)
        self.tree.pack(fill="both", expand=True, padx=8, pady=8)

        load_data(self)

        self.btn_frame = tk.Frame(self.tab)
        self.btn_frame.pack(pady=4)

        tk.Button(self.btn_frame, text="Add", command=lambda: add_record(self), width=12).grid(row=0, column=0, padx=4)
        tk.Button(self.btn_frame, text="Update", command=lambda: update_record(self), width=12).grid(row=0, column=1, padx=4)
        tk.Button(self.btn_frame, text="Delete", command=lambda: delete_record(self), width=12).grid(row=0, column=2, padx=4)
        tk.Button(self.btn_frame, text="Clear", command=lambda: clear_fields(self), width=12).grid(row=0, column=3, padx=4)
        tk.Button(self.btn_frame, text="Export", command=lambda: export_to_csv(self.tree), width=12).grid(row=0, column=4, padx=4)

        def on_tree_select(event):
            selected = self.tree.focus()
            if selected:
                values = self.tree.item(selected, 'values')
                for i, col in enumerate(self.col_names):
                    if col != self.primary_key:
                        self.entry_vars[col].set(values[i])

        self.tree.bind("<<TreeviewSelect>>", on_tree_select)

        cursor.close()
        conn.close()
    # def get_data(self):
    #     add_record(self.entries, self.table_name)




if __name__ == "__main__":

    # conn = connect_db()
    # cursor = conn.cursor()

    root = tk.Tk()
    root.title("KFood POS System")
    root.state("zoomed")  # Fullscreen
    # root.geometry("1366x768")

    # table_name = "EMPLOYEES"
    schema_name = "kfood_pos"
    tables = [
        "CUSTOMERS", "EMPLOYEES", "ORDERS", "MENU_ITEMS", "ORDER_DETAILS",
        "PAYMENTS", "SUPPLIERS", "INVENTORY", "PURCHASES", "PURCHASE_DETAILS"
    ]
    # tables = get_table_names()


# ---------------------- Main Window ---------------------- #
    notebook = ttk.Notebook(root)
    notebook.pack(expand=1, fill='both')

# ---------------------- Search Tab ---------------------- #
    search_tab = ttk.Frame(notebook)
    notebook.add(search_tab, text="Search")

    search_frame = tk.Frame(search_tab)
    search_frame.pack(padx=8, pady=8, fill='none')

    all_entry_vars = {}
    # for table in tables:
    #     Search_Form(table, schema_name, search_frame)

################################
    selected_table = tk.StringVar()
    table_combo = ttk.Combobox(search_frame, textvariable=selected_table, values=tables, state='readonly', width=25)
    table_combo.grid(row=0, column=0, padx=8, pady=8)
    table_combo.set("CUSTOMERS")

    search_area = tk.Frame(search_tab)
    search_area.pack()

    search_entries = {}
    columns = []

    table_combo.bind("<<ComboboxSelected>>", Search_Form)
    Search_Form()
################################

    button_frame = tk.Frame(search_tab)
    button_frame.pack(pady=8)
    tk.Button(button_frame, text="Serach", command=lambda: search_record(selected_table, search_entries, Search_tree, columns), width=12).grid(row=0, column=0, padx=4)
    # tk.Button(button_frame, text="Clear", command=lambda: clear_fields_search(all_entry_vars), width=12).grid(row=0, column=1, padx=4)
    tk.Button(button_frame, text="Export", command=lambda: export_to_csv(Search_tree), width=12).grid(row=0, column=2, padx=4)

    tree_frame = tk.Frame(search_tab)
    tree_frame.pack(padx=8, pady=8, fill='both', expand=True)
    Search_tree = ttk.Treeview(tree_frame)
    Search_tree.pack(fill="both", expand=True, padx=8, pady=8)

    # scrollbar = ttk.Scrollbar(tree_frame, orient='vertical', command=Search_tree.yview)
    # scrollbar.pack(side='right', fill='y')
    # Search_tree.configure(yscrollcommand=scrollbar.set)

# ---------------------- Modify Tab ---------------------- #
    modify_tab = ttk.Frame(notebook)
    notebook.add(modify_tab, text="Modify")

    modify_notebook = ttk.Notebook(modify_tab)
    modify_notebook.pack(padx=8, pady=8, fill='both', expand=True)

    for table in tables:
        Modify(table, schema_name, modify_notebook)

    root.mainloop()
