# Define a ShoppingListApp which inherits from the Tk base class.
import tkinter as tk
from tkinter import messagebox

from tutorial_4.model.ShoppingItem import ShoppingItem

shoppingListItems = []
# ShoppingListApp is inheriting from tkinter instead
class ShoppingListApp(tk.Tk):
    # constructor to create an object called ShoppingListApp child of tkinter class (so has access to all methods in tkinter)
    def __init__(self):
        # super is used in inheritance so we now inherit all methods from Tkinter
        super().__init__()
        self.title("Shopping List App")
        self.geometry("400x400")

        # defining all the object using self because it's the shoppingCartItem not the tkinter one
        self.name_label = tk.Label(self, text="Item Name:")
        self.name_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.price_label = tk.Label(self, text="Item Price:")
        self.price_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.price_entry = tk.Entry(self)
        self.price_entry.grid(row=1, column=1, padx=10, pady=5)

        self.add_button = tk.Button(self, text="Add Item", command=self.add_item)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.delete_button = tk.Button(self, text="Delete Item", command=self.delete_item)
        self.delete_button.grid(row=2, column=2, pady=10)

        self.listbox = tk.Listbox(self, height=10,
                          width=30,
                          bg="grey",
                          activestyle='dotbox',
                          font="Helvetica",
                          fg="yellow")

        self.listbox.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

        self.cart_quantity_label = tk.Label(self, text="Cart Quantity:")
        self.cart_quantity_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)

        self.cart_quantity_value_label = tk.Label(self, text="0")  # Placeholder starts with 0
        self.cart_quantity_value_label.grid(row=4, column=1, padx=10, pady=5)

    def add_item(self):
        # get the item_name value from object created above
        item_name = self.name_entry.get()
        # try except statement. The code is tried, that's what the try is for.
        try:
            # parsing input to float
            item_price = float(self.price_entry.get())
            # so if the code fails to parse due to it not being a number raise ValueError Exception
        except ValueError:
            # display message box with error, if you did not catch the exception in this except condition the application would crash
            messagebox.showerror(title="Input format error", message="Invalid price entered!")
            return
        # when input checked create a ShoppingItem object called item and input the two parameters name and price as described in the ShoppngItem class
        item = ShoppingItem(item_name, item_price)

        # Insert item object into list box to store it
        self.listbox.insert("end",item)

        # add ShoppingItem object to the shopping cart
        shoppingListItems.append(item)

        # Clear the entries
        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        # call method to display amount of items in basket
        self.getCartQuantity()

    def delete_item(self):
        itemName = self.name_entry.get()  # Get the item name from the entry

        # validate itemName variable is not null or empty
        if not itemName:
            # print message box if it is
            messagebox.showwarning("Input Error", "Please enter an item name to delete.")
            return
        # use check method to see if the item is in the cart
        found_item = self.check_for_item(itemName)

        # if check basket returned true run the code block
        if found_item:
            # remove the item from the list
            shoppingListItems.remove(found_item)  # Remove from the internal list
            # Find the index of the item in the listbox and delete it
            index = self.listbox.get(0, tk.END).index(str(found_item))
            self.listbox.delete(index)  # Remove from the listbox
            # Clear the entry fields
            self.name_entry.delete(0, tk.END)
            self.price_entry.delete(0, tk.END)
            # call method to display amount of items in basket
            self.getCartQuantity()
        else:
            # if the item is not in the basket print item not found (could be done as try except statement instead)
            messagebox.showinfo("Item Not Found", f"{itemName} is not in the shopping list.")

    # helper method to find if item in cart takes a string argument of item name
    def check_for_item(self, itemName):
        # loop through all the item objects in ShoppingListItems
        for item in shoppingListItems:
            # check if the itemName passed into the function is the same as the name of an item in the cart
            if itemName == item.name:
                # if so return true
                return item
        return None

    # Function to keep track of the cart Quantity
    def getCartQuantity(self):
        # replace label with the quantity value of the cart
        self.cart_quantity_value_label.config(text=str(len(shoppingListItems)))

# Run the project
app = ShoppingListApp()
app.mainloop()