class ShoppingItem:
    name = "Unnamed Item"
    price = 0.00
    quantity = 0

    def __init__(self, name=None, price=None, quantity=None):
        if name is not None:
            self.name = name
        if price is not None:
            self.price = price
        if quantity is not None:
            self.quantity = quantity

    def __str__(self):
        return f"Item: {self.name}, Price: €{self.price:.2f}, Quantity: {self.quantity}"

    def __repr__(self):
        return self.__str__()