from updated_cart_tutorial_6.model.Tayto import Tayto
from updated_cart_tutorial_6.model.ShoppingCart import ShoppingCart
from updated_cart_tutorial_6.model.LineItem import LineItem

# Creating an object of Tayto class
taytoCheese = Tayto("Cheese and onion Taytos", 1.50, 30)
# Call get price for taytoCheese object
taytoCheese.getPrice()

lineItem2 = LineItem(taytoCheese, 3)


cart = ShoppingCart()
cart.add_item(lineItem2)
print(cart)
print(cart.cartTotal())