from updated_cart_tutorial_6.model.LineItem import LineItem
from updated_cart_tutorial_6.converter.ConvertToCurrency import convertNumberToPrice


class ShoppingCart:
    lineItems = []

    def __init__(self):
        self.lineItems = []

    def add_item(self, item):
        self.lineItems.append(item)

    def cartTotal(self):
        cartPrice = 0.0
        for lineItem in self.lineItems:

            cartPrice += lineItem.totalPrice

        return convertNumberToPrice(cartPrice)


    def __str__(self):
        if not self.lineItems:
            return "Shopping Cart is empty."

        cart_items_str = "Shopping Cart:\n"
        for lineItem in self.lineItems:
            cart_items_str += (f"Product: {lineItem.product.name}, Quantity: {lineItem.itemQuantity}"
                               f", Total Price: {lineItem.totalPrice}\n")

        return cart_items_str.strip()
