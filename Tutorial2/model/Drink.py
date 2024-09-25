from Tutorial2.model.Product import Product

# Inherit characteristics and methods from parent Product
class Drink(Product):
    # add unique characteristic for Drinks
    def __init__(self, name, price, millilitres):
        # super used to inherit characteristics from Product must inherit all of them
        super().__init__(name, price)
        self.millilitres = millilitres

    # must implement methods from parent, passed here because you would'nt just buy a drink it would be a specific drink
    def getPrice(self):
        pass