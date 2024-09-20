from abc import ABC, abstractmethod

# Abstract Base Class
class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def getPrice(self):
        pass