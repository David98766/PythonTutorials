from Tutorial2.model.Product import Product



class LineItem:


    def __init__(self, product: Product, itemQuantity):
        self.itemQuantity = itemQuantity
        self.product = product
        self.totalPrice = product.price * itemQuantity
