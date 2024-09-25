from Tutorial2.model.Coke import Coke
from Tutorial2.model.Tayto import Tayto

# Create Object of Coke Class so you can access
coke = Coke("Coke", 2.50, 500)
# Call get price method for Coke object
coke.getPrice()

# Creating an object of Tayto class
taytoCheese = Tayto("Cheese and onion Taytos", 1.50, 30)
# Call get price for taytoCheese object
taytoCheese.getPrice()