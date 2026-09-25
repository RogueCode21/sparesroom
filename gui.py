import tkinter as tk
from tkinter import messagebox
import inventory

def add_part_submit():
    try:
        inventory.add_part(
            name_entry.get(),
            category_entry.get(),
            int(qty_entry.get()),
            int(reorder_entry.get()),
            description_entry.get()
        )
        messagebox.showinfo("Success", f"Added {name_entry.get()}")
    except ValueError:
        messagebox.showerror("Error", "Quantity and reorder point must be numbers.")

root = tk.Tk()
root.title("SparesRoom")

tk.Label(root, text="Part name:").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Category:").grid(row=1, column=0)
category_entry = tk.Entry(root)
category_entry.grid(row=1, column=1)

tk.Label(root, text="Quantity:").grid(row=2, column=0)
qty_entry = tk.Entry(root)
qty_entry.grid(row=2, column=1)

tk.Label(root, text="Reorder point:").grid(row=3, column=0)
reorder_entry = tk.Entry(root)
reorder_entry.grid(row=3, column=1)

tk.Label(root, text="Description:").grid(row=4, column=0)
description_entry = tk.Entry(root)
description_entry.grid(row=4, column=1)

tk.Button(root, text="Add Part", command=add_part_submit).grid(row=5, column=0, columnspan=2)

root.mainloop()