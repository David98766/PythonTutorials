from Tutorial2.model.Product import Product

class Crisp(Product):
    def __init__(self, name, price, grams):
        super().__init__(name, price)
        self.grams = grams

    def getPrice(self):
        pass