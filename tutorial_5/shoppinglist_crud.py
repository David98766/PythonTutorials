import tkinter as tk
from tkinter import ttk, messagebox

from model.shopping_item import ShoppingItem

class ShoppingListApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Shopping List App")
        self.geometry("500x400")
        
        self.items = []  # List to store ShoppingItem objects

        # Widgets
        self.name_label = ttk.Label(self, text="Item Name:")
        # sticky="w" means the widget will stick to the left (west) side of the grid cell.
        self.name_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        self.name_entry = ttk.Entry(self)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.price_label = ttk.Label(self, text="Item Price:")
        self.price_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

        self.price_entry = ttk.Entry(self)
        self.price_entry.grid(row=1, column=1, padx=10, pady=5)

        self.add_button = ttk.Button(self, text="Add", command=self.add_item)
        self.add_button.grid(row=2, column=0, pady=10)

        self.update_button = ttk.Button(self, text="Update", command=self.update_item)
        self.update_button.grid(row=2, column=1, pady=10)

        self.delete_button = ttk.Button(self, text="Delete", command=self.delete_item)
        self.delete_button.grid(row=2, column=2, pady=10)

        self.listbox = tk.Listbox(self, height=15, width=50)
        self.listbox.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

        # we are binding a method (on_listbox_select) to the action of selecting a line of the listbox
        # In other words, we are executing on_listbox_select everytime a line of the listbox is selected
        # '<<ListboxSelect>>' is an event
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

    # Add this method
    def get_selected_index(self):
        # Getting the index of the currently selected item in the Listbox
        index = self.listbox.curselection()

        # curselection is a native method for Tkinter
        # curselection retrieves the line number (index) of the selected item in a listbox (starts with 0)
        # index = line number
        print(index)

        # returning that variable so other methods can use it
        return index

    # Notice this method takes an event, remember we bound this method to '<<ListboxSelect>>' earlier?
    def on_listbox_select(self, event):
        # calling the get_selected_index method
        index = self.get_selected_index()

        # If an item is selected, proceed (index will be empty if no selection is made)
        if index:
            # Retrieve the selected item from the internal items list using the index
            item = self.items[index[0]]
            # Clearing the name entry field and inserting the name of the selected item
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, item.name)
            # Clearing the price entry field and inserting the price of the selected item
            self.price_entry.delete(0, tk.END)
            self.price_entry.insert(0, str(item.price))

    def update_item(self):

        index = self.get_selected_index()
        # If no item is selected, show a message prompting the user to select an item and return
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

        index = self.get_selected_index()

        if not index:
            messagebox.showinfo("Info", "Please select an item from the list to delete.")
            return

        del self.items[index[0]]
        self.listbox.delete(index[0])

        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

if __name__ == "__main__":
    app = ShoppingListApp()
    app.mainloop()
