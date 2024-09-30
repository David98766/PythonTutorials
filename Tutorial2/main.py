from Tutorial2.model.Coke import Coke
from Tutorial2.model.Tayto import Tayto
from Tutorial2.model.ShoppingCart import ShoppingCart
from Tutorial2.model.LineItem import LineItem

# Create Object of Coke Class so you can access
coke = Coke("Coke", 2.50, 500)
# Call get price method for Coke object
coke.getPrice()

# Creating an object of Tayto class
taytoCheese = Tayto("Cheese and onion Taytos", 1.50, 30)
# Call get price for taytoCheese object
taytoCheese.getPrice()

lineItem1 = LineItem(coke, 2)
lineItem2 = LineItem(taytoCheese, 3)


cart = ShoppingCart()
cart.add_item(lineItem1)
cart.add_item(lineItem2)
print(cart)
print(cart.cartTotal())