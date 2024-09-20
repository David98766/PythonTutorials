from Tutorial2.model.Product import Product

class Drink(Product):
    def __init__(self, name, price, millilitres):
        super().__init__(name, price)
        self.millilitres = millilitres

    def getPrice(self):
        pass