# importing abstract to make the class a parent

# Abstract Base Class
class Product:
    # Attributes specific to all products
    def __init__(self, name, price):
        self.name = name
        self.price = price

# abstract method will be passed, child classes will have their own implementation of the method (Polymorphism)
    def getPrice(self):
        pass