from db import connect_db


def search_record(selected_table, search_entries, Search_tree, columns):
    print("search_record")
    table = selected_table.get()
    if not table:
        return

    conn = connect_db()
    cursor = conn.cursor()
    conditions = []
    values = []

    for col, entry in search_entries.items():
        val = entry.get().strip()
        if val:
            conditions.append(f"{col} LIKE %s")
            values.append(f"%{val}%")

    query = f"SELECT * FROM {table}"
    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    try:
        cursor.execute(query, values)
        rows = cursor.fetchall()

        # Search_tree.delete(*Search_tree.get_children())
        for item in Search_tree.get_children():
            Search_tree.delete(item)
        Search_tree["columns"] = columns
        Search_tree["show"] = "headings"
        for col in columns:
            Search_tree.heading(col, text=col)
            Search_tree.column(col, width=100, anchor='center')
        for row in rows:
            Search_tree.insert('', 'end', values=row)

    except Exception as e:
        print(f"Error: {e}")

    cursor.close()
    conn.close()




def clear_fields_search(all_entry_vars):
    # Clear the search entry and treeview
    for table_name, entry_vars in all_entry_vars.items():
        for var in entry_vars.values():
            var.set("")
    print("clear_fields_search")