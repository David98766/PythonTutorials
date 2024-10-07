from updated_cart_tutorial_6.model.Product import Product

# Inherit characteristics and methods from parent Product
class Crisp(Product):
    # add unique characteristic for Crisp class
    def __init__(self, name, price, grams):
        # super used to inherit characteristics from Product must inherit all of them
        super().__init__(name, price)
        self.grams = grams

    # must implement methods from parent, passed here because you would'nt just buy a Crisps it would be a specific pack of Crisps
    def getPrice(self):
        pass