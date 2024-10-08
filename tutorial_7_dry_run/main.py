import tkinter as tk
from tkinter import messagebox
from model.contact import Contact


# Main part of the application to launch the Tkinter window and the contact list app.
def main():
    root = tk.Tk()  # Create the main Tkinter window
    root.title("Contact List App")  # Set the window title
    app = ContactApp(root)  # Create an instance of the ContactApp class, passing the root window
    root.mainloop()  # Start the Tkinter event loop to display the window and handle events

# The ContactApp class defines the main functionality and GUI of the contact list application.
class ContactApp:
    def __init__(self, root):
        # IMPORTANT
        self.contacts = []  # List to store contacts.

        # Create Labels for input fields (Name, Phone, Address).
        self.name_label = tk.Label(root, text="Name")
        self.phone_label = tk.Label(root, text="Phone")
        self.address_label = tk.Label(root, text="Address")

        # Create Entry widgets to allow user to input name, phone, and address.
        self.name_entry = tk.Entry(root)
        self.phone_entry = tk.Entry(root)
        self.address_entry = tk.Entry(root)

        # Create Buttons for adding, updating, and deleting contacts.
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)

        # Create a Listbox to display the list of contacts.
        self.listbox = tk.Listbox(root)
        # Bind the listbox to an event that loads the selected contact's details into the input fields.
        self.listbox.bind('<<ListboxSelect>>', self.load_contact)

        # Arrange all widgets using grid layout.
        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)
        self.phone_label.grid(row=1, column=0)
        self.phone_entry.grid(row=1, column=1)
        self.address_label.grid(row=2, column=0)
        self.address_entry.grid(row=2, column=1)

        self.add_button.grid(row=3, column=0)
        self.update_button.grid(row=3, column=1)
        self.delete_button.grid(row=3, column=2)
        self.listbox.grid(row=0, column=3, rowspan=4)

    # Helper function to clear the input fields (used after add/update/delete operations).
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    # Function to add a contact to the list and update the listbox.
    def add_contact(self):
        # Get values from the entry fields.
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()

        # Basic validation for phone number (it must be 10 digits).
        if not phone.isdigit() or len(phone) != 10:
            messagebox.showerror("Invalid Input", "Phone number must be 10 digits.")
            return

        # Create a new Contact object and add it to the contact list.
        contact = Contact(name, phone, address)
        # APPEND = ADD TO LIST aka we are adding the new Contact to the contacts list
        self.contacts.append(contact)

        # Update the listbox to reflect the newly added contact.
        self.update_listbox()

        # Clear the entry fields after adding a contact.
        self.clear_entries()

    def get_selected_index(self):
        # Getting the index of the currently selected item in the Listbox
        index = self.listbox.curselection()
        # curselection retrieves the line number (index) of the selected item in a listbox (starts with 0)
        # index = line number
        print(index)
        # returning that variable so other methods can use it
        return index

    # Function to load the details of the selected contact from the listbox into the entry fields.
    def load_contact(self, event):
        index = self.listbox.curselection()  # Get the selected contact's index.
        if index:
            index = index[0]
            contact = self.contacts[index]

            # Fill the entry fields with the contact's current details.
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(tk.END, contact.name)

            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(tk.END, contact.phone)

            self.address_entry.delete(0, tk.END)
            self.address_entry.insert(tk.END, contact.address)

    # Function to update the selected contact's details in the list.
    def update_contact(self):
        index = self.listbox.curselection()  # Get the selected contact's index.
        if not index:
            messagebox.showerror("No Selection", "Please select a contact to update.")
            return

        # Get the selected contact and update its details.
        index = index[0]
        contact = self.contacts[index]

        # Update contact details from the entry fields.
        contact.name = self.name_entry.get()
        contact.phone = self.phone_entry.get()
        contact.address = self.address_entry.get()

        # Validate the updated phone number.
        if not contact.phone.isdigit() or len(contact.phone) != 10:
            messagebox.showerror("Invalid Input", "Phone number must be 10 digits.")
            return

        # Update the listbox to reflect the updated contact details.
        self.update_listbox()

        # Clear the entry fields after updating.
        self.clear_entries()

    # Function to delete the selected contact from the list and listbox.
    def delete_contact(self):
        index = self.listbox.curselection()  # Get the selected contact's index.
        if not index:
            messagebox.showerror("No Selection", "Please select a contact to delete.")
            return

        # Delete the selected contact from the contact list.
        index = index[0]
        del self.contacts[index]

        # Update the listbox to reflect the removal of the contact.
        self.update_listbox()

        # Clear the entry fields after deleting.
        self.clear_entries()

    # Helper function to update the listbox with the current contact list.
    def update_listbox(self):
        self.listbox.delete(0, tk.END)  # Clear the listbox.
        for contact in self.contacts:
            # Insert each contact's name into the listbox.
            self.listbox.insert(tk.END, contact.name)


main()