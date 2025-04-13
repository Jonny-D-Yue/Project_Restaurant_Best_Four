

def search_record():
    # # Get the table name and search criteria from the user
    # table_name = table_name_var.get()
    # search_criteria = search_entry.get()

    # # Construct the SQL query
    # query = f"SELECT * FROM {table_name} WHERE {search_column} LIKE %s"
    # cursor.execute(query, (f"%{search_criteria}%",))

    # # Fetch the results
    # results = cursor.fetchall()

    # # Clear the treeview before inserting new data
    # for item in tree.get_children():
    #     tree.delete(item)

    # # Insert the results into the treeview
    # for row in results:
    #     tree.insert("", "end", values=row)
    print("search_record")

def clear_fields_search(all_entry_vars):
    # Clear the search entry and treeview
    for table_name, entry_vars in all_entry_vars.items():
        for var in entry_vars.values():
            var.set("")
    print("clear_fields_search")