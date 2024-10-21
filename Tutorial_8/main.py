import tkinter as tk
from tkinter import messagebox

#Contact class

class Contact:
    name = "Unnamed Contact"
    phone = "000-000-0000"
    address = "No Address"

    def __init__(self, name=None, phone=None, address=None):
        if name is not None:
            self.name = name
        if phone is not None:
            self.phone = phone
        if address is not None:
            self.address = address

    def __str__(self):
        return f"Contact: {self.name}, Phone: {self.phone}, Address: {self.address}"

    def __repr__(self):
        return self.__str__()

#Application class
# Inheritance example
class ContactApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contact App")
        self.geometry("500x500")

        self.contacts = []  # List to store Contact objects

        # Widgets
        self.name_label = tk.Label(self, text="Contact Name:")
        self.name_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label = tk.Label(self, text="Contact Phone:")
        self.phone_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

        self.phone_entry = tk.Entry(self)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.address_label = tk.Label(self, text="Contact Address:")
        self.address_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)

        self.address_entry = tk.Entry(self)
        self.address_entry.grid(row=2, column=1, padx=10, pady=5)

        self.add_button = tk.Button(self, text="Add", command=self.add_contact)
        self.add_button.grid(row=3, column=0, pady=10)

        self.update_button = tk.Button(self, text="Update", command=self.update_contact)
        self.update_button.grid(row=3, column=1, pady=10)

        self.delete_button = tk.Button(self, text="Delete", command=self.delete_contact)
        self.delete_button.grid(row=3, column=2, pady=10)

        self.listbox = tk.Listbox(self, height=15, width=50)
        self.listbox.grid(row=4, column=0, columnspan=3, padx=10, pady=5)

        self.listbox.bind('<<ListboxSelect>>', self.on_listbox_select)

    def add_contact(self):
        contact_name = self.name_entry.get()
        contact_phone = self.phone_entry.get()
        contact_address = self.address_entry.get()

        contact = Contact(contact_name, contact_phone, contact_address)
        self.contacts.append(contact)
        self.listbox.insert(tk.END, str(contact))

        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def on_listbox_select(self, event):
        index = self.listbox.curselection()
        if index:
            contact = self.contacts[index[0]]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, contact.name)
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, str(contact.phone))
            self.address_entry.delete(0, tk.END)
            self.address_entry.insert(0, str(contact.address))

    def update_contact(self):
        index = self.listbox.curselection()
        if not index:
            messagebox.showinfo("Info", "Please select a contact from the list to update.")
            return

        contact_name = self.name_entry.get()
        contact_phone = self.phone_entry.get()
        contact_address = self.address_entry.get()

        updated_contact = Contact(contact_name, contact_phone, contact_address)
        self.contacts[index[0]] = updated_contact
        self.listbox.delete(index[0])
        self.listbox.insert(index[0], str(updated_contact))
        self.listbox.selection_set(index)

    def delete_contact(self):
        index = self.listbox.curselection()
        if not index:
            messagebox.showinfo("Info", "Please select a contact from the list to delete.")
            return

        del self.contacts[index[0]]
        self.listbox.delete(index[0])

        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)


#Program

if __name__ == "__main__":
    app = ContactApp()
    app.mainloop()