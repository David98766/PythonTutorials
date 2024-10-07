# importing abstract to make the class a parent
from abc import ABC, abstractmethod

# Abstract Base Class
class Product(ABC):
    # Attributes specific to all products
    def __init__(self, name, price):
        self.name = name
        self.price = price

# abstract method will be passed, child classes will have their own implementation of the method (Polymorphism)
    @abstractmethod
    def getPrice(self):
        pass