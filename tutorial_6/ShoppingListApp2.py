import tkinter as tk
from tkinter import messagebox
from tutorial_6.model.ShoppingItem import ShoppingItem

class ShoppingListApp2(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Shopping List App")
        self.geometry("500x400")

        self.items = []  # List to store ShoppingItem objects

        # Widgets
        self.name_label = tk.Label(self, text="Item Name:")
        self.name_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.price_label = tk.Label(self, text="Item Price:")
        self.price_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

        self.price_entry = tk.Entry(self)
        self.price_entry.grid(row=1, column=1, padx=10, pady=5)

        self.add_button = tk.Button(self, text="Add", command=self.add_item)
        self.add_button.grid(row=2, column=0, pady=10)

        self.update_button = tk.Button(self, text="Update", command=self.update_item)
        self.update_button.grid(row=2, column=1, pady=10)

        self.delete_button = tk.Button(self, text="Delete", command=self.delete_item)
        self.delete_button.grid(row=2, column=2, pady=10)

        self.listbox = tk.Listbox(self, height=15, width=50)
        self.listbox.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

        self.listbox.bind('<<ListboxSelect>>', self.on_listbox_select)

    def add_item(self):
        item_name = self.name_entry.get()
        try:
            item_price = float(self.price_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid price entered!")
            return

        item = ShoppingItem(item_name, item_price)
        self.items.append(item)
        self.listbox.insert(tk.END, str(item))

        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

    def on_listbox_select(self, event):
        index = self.listbox.curselection()
        if index:
            item = self.items[index[0]]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, item.name)
            self.price_entry.delete(0, tk.END)
            self.price_entry.insert(0, str(item.price))

    def update_item(self):
        index = self.listbox.curselection()
        if not index:
            messagebox.showinfo("Info", "Please select an item from the list to update.")
            return

        item_name = self.name_entry.get()
        try:
            item_price = float(self.price_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid price entered!")
            return

        updated_item = ShoppingItem(item_name, item_price)
        self.items[index[0]] = updated_item
        self.listbox.delete(index[0])
        self.listbox.insert(index[0], str(updated_item))
        self.listbox.selection_set(index)

    def delete_item(self):
        index = self.listbox.curselection()
        if not index:
            messagebox.showinfo("Info", "Please select an item from the list to delete.")
            return

        del self.items[index[0]]
        self.listbox.delete(index[0])

        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)


if __name__ == "__main__":
    app = ShoppingListApp2()
    app.mainloop()
