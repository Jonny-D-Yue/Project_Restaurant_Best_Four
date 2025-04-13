import csv
from tkinter import filedialog
from tkinter import messagebox

def export_to_csv(treeview):
    file_path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv")],
        title="Save as"
    )

    if not file_path:
        return

    try:
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            columns = treeview["columns"]
            writer.writerow(columns)

            for item in treeview.get_children():
                row = [treeview.item(item)['values'][i] for i in range(len(columns))]
                writer.writerow(row)

        messagebox.showinfo("Success", f"Data successfully exported to {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to export data:\n{e}")