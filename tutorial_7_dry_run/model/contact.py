# The Contact class defines a contact with name, phone, and address attributes.
class Contact:
    name = "Unnamed Contact"
    phone = "000-000-0000"
    address = "No Address"

    # Initialize a contact object with optional name, phone, and address parameters.
    def __init__(self, name=None, phone=None, address=None):
        if name is not None:
            self.name = name
        if phone is not None:
            self.phone = phone
        if address is not None:
            self.address = address

    # String representation of the contact, used in listbox and debugging.
    def __str__(self):
        return f"Contact: {self.name}, Phone: {self.phone}, Address: {self.address}"

    def __repr__(self):
        return self.__str__()
