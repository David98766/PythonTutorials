class ShoppingItem:

    name = "Unnamed Item"
    price = 0.00

    # constructor to create ShoppingItem object needs two parameters if you don't fill them in, it will default to the initialized attributes above
    def __init__(self, name=None, price=None):
        if name is not None:
            self.name = name
        if price is not None:
            self.price = price

    def __str__(self):
        return f"Item: {self.name}, Price: €{self.price:.2f}"

    def __repr__(self):
        return f"Item: {self.name}, Price: €{self.price:.2f}"