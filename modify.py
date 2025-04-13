from tkinter import messagebox
from db import connect_db

def clear_fields(form_obj):
    for var in form_obj.entry_vars.values():
        var.set("")
    form_obj.tree.selection_remove(form_obj.tree.selection())
    print(f"clear_fields {form_obj.table_name}")


def load_data(form_obj):
    conn = connect_db()
    cursor = conn.cursor()
    for item in form_obj.tree.get_children():
        form_obj.tree.delete(item)
    cursor.execute(f"SELECT * FROM {form_obj.table_name}")
    rows = cursor.fetchall()
    form_obj.tree["columns"] = form_obj.col_names
    form_obj.tree["show"] = "headings"
    for col in form_obj.col_names:
        form_obj.tree.heading(col, text=col)
        form_obj.tree.column(col, anchor="center", width=120)
    for row in rows:
        form_obj.tree.insert("", "end", values=row)
    cursor.close()
    conn.close()
    print(f"load_data {form_obj.table_name}")


def on_tree_select(form_obj):
    selected = form_obj.tree.focus()
    if selected:
        values = form_obj.tree.item(selected, 'values')
        for i, col in enumerate(form_obj.col_names):
            if col != form_obj.primary_key:
                form_obj.entry_vars[col].set(values[i])


def add_record(form_obj):
    conn = connect_db()
    cursor = conn.cursor()
    values = [form_obj.entry_vars[col].get() for col in form_obj.col_names if col != form_obj.primary_key]
    # values = [form_obj.entry_vars[col].get() for col in form_obj.columns]
    if any(v == "" for v in values):
        messagebox.showwarning("Lack of information", "Please fill enough!")
        return
    placeholders = ', '.join(['%s'] * len(values))
    fields = ', '.join([col for col in form_obj.col_names if col != form_obj.primary_key])
    # fields = ', '.join([col for col in form_obj.columns])
    try:
        cursor.execute(f"INSERT INTO {form_obj.table_name} ({fields}) VALUES ({placeholders})", values)
        conn.commit()
        load_data(form_obj)
        clear_fields(form_obj)
    except Exception as e:
        messagebox.showerror("Error", str(e))
    cursor.close()
    conn.close()
    print(f"add_record {form_obj.table_name}")


def update_record(form_obj):
    conn = connect_db()
    cursor = conn.cursor()
    selected = form_obj.tree.focus()
    if not selected:
        messagebox.showwarning("Not choose", "Please choose a record to update!")
        return
    values = form_obj.tree.item(selected, 'values')
    pk_value = values[0]
    new_values = [form_obj.entry_vars[col].get() for col in form_obj.col_names if col != form_obj.primary_key]
    if any(v == "" for v in new_values):
        messagebox.showwarning("Lack of information", "Please fill enough!!")
        return
    set_clause = ', '.join([f"{col}=%s" for col in form_obj.col_names if col != form_obj.primary_key])
    try:
        cursor.execute(f"UPDATE {form_obj.table_name} SET {set_clause} WHERE {form_obj.primary_key}=%s", (*new_values, pk_value))
        conn.commit()
        load_data(form_obj)
        clear_fields(form_obj)
    except Exception as e:
        messagebox.showerror("Error", str(e))
    cursor.close()
    conn.close()
    print(f"update_record {form_obj.table_name}")


def delete_record(form_obj):
    conn = connect_db()
    cursor = conn.cursor()
    selected = form_obj.tree.focus()
    if not selected:
        messagebox.showwarning("Not choose", "Please choose a record to delete!")
        return
    values = form_obj.tree.item(selected, 'values')
    pk_value = values[0]
    if messagebox.askyesno("Confirm", f"Do you want to delete {pk_value}?"):
        cursor.execute(f"DELETE FROM {form_obj.table_name} WHERE {form_obj.primary_key}=%s", (pk_value,))
        conn.commit()
        load_data(form_obj)
        clear_fields(form_obj)
    cursor.close()
    conn.close()
    print(f"delete_record {form_obj.table_name}")
