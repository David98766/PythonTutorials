import tkinter as tk
from tkinter import messagebox

#Contact class

class Contact:
    # defining variables
    name = "Unnamed Contact"
    phone = "000-000-0000"
    address = "No Address"

    # initializing the Contact Object
    #Assigning none values by default
    def __init__(self, name=None, phone=None, address=None):
        # if variable HAS A VALUE (is not none) then assign it that value.
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

# REMEMBER to comment the following:
# "This is an example of Encapsulation, which is a core concept of OOP."
# put that comment above any class declaration (like the line below)
class ContactApp(tk.Tk):
    def __init__(self):
        # Put this comment above the word "super" in your code
        # "This is an example of inheritance, a core concept of OOP"
        super().__init__()
        # Setting title of Application
        self.title("Contact App")
        # Setting size of Application
        self.geometry("500x500")

        # LIST and LISTBOX ARE SEPARATE, they are not the same thing
        # the contents of the list is displayed on the listbox
        self.contacts = []  # List to store Contact objects

        # Widgets
        #COPY AND PASTE, takes too long to type each individually, test will be over
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

        # REMEMBER THIS LINE, it is binding the 'event' of a user selecting a
        # line on a listbox to the method "on_listbox_select"
        # If you forget this line your program will not work correctly
        self.listbox.bind('<<ListboxSelect>>', self.on_listbox_select)

    # Adding contact to the LIST
    def add_contact(self):
        contact_name = self.name_entry.get()
        contact_phone = self.phone_entry.get()
        contact_address = self.address_entry.get()

        # big C contact is the Contact object (class)

        contact = Contact(contact_name, contact_phone, contact_address)
        # append = add
        # small c contacts (With an s) is the LIST
        # so here we are adding an 'object' (which carries information)
        # to the list
        self.contacts.append(contact)
        # adding that contact you just created to the END of the LISTBOX
        # converting contact to a string.
        self.listbox.insert(tk.END, str(contact))

        # clearing the entries from the text entry boxes in your application.
        # if you want you can use the clear_entries(self) method
        # from tutorial 7 instead, probably would get you a few extra marks
        # but if you do you will have to change some code
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    # this is the method we bound to the listbox select event above.
    def on_listbox_select(self, event):
        # index = line number (starts with 0)
        # so index = current selection of the listbox
        # (contact you have clicked on in the listbox)
        index = self.listbox.curselection()
        # AKA if there is a line selcted
        if index:

            contact = self.contacts[index[0]]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, contact.name)
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, str(contact.phone))
            self.address_entry.delete(0, tk.END)
            self.address_entry.insert(0, str(contact.address))

    # essentially changing the details of a contact
    def update_contact(self):
        index = self.listbox.curselection()
        if not index:
            messagebox.showinfo("Info", "Please select a contact from the list to update.")
            return

        # getting text from text entry boxes
        contact_name = self.name_entry.get()
        contact_phone = self.phone_entry.get()
        contact_address = self.address_entry.get()

        # deleting old entry, putting new entry in
        updated_contact = Contact(contact_name, contact_phone, contact_address)
        self.contacts[index[0]] = updated_contact
        self.listbox.delete(index[0])
        self.listbox.insert(index[0], str(updated_contact))
        self.listbox.selection_set(index)

    # This is mostly re-used code
    def delete_contact(self):
        index = self.listbox.curselection()
        if not index:
            messagebox.showinfo("Info", "Please select a contact from the list to delete.")
            return

        # this del line is new, it means delete the selected contact from
        # the LIST
        del self.contacts[index[0]]
        # This line is deleting from the LISTBOX
        # REMEMBER List and listbox are not the same, they need
        # to be dealt with separately
        self.listbox.delete(index[0])

        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

#Program

# DO NOT FORGET THIS METHOD IF YOU DO YOUR PROJECT WILL NOT RUN AT ALL
# Simon said this will cap your grade at 60%
if __name__ == "__main__":
    app = ContactApp()
    app.mainloop()