import random

# We have a list of prices, but we want a list of prices with VAT added
prices = [1.09, 23.56, 57.84, 4.56, 6.78]
TAX_RATE = .08

#this method is called when it is passed to the map function
def get_price_with_tax(price):
    return price * (1 + TAX_RATE)

# We can use a map for this easily
# passing a function and a list for the function to iterate through and map values
# returned by the function to variables in the list
priceWithVAT = map(get_price_with_tax, prices)
# then we convert the map to a list so we can print it
listPriceWithVAT = list(priceWithVAT)
print("Prices List using a map", listPriceWithVAT)

# Better cleaner Solution use Comprehension
listPriceWithVAT2 = [get_price_with_tax(price) for price in prices]
print("Comprehension List for Prices", listPriceWithVAT2)

# making the function above is optional you can make everything in the one line of code
listPriceWithVAT3 = [price*(1 + TAX_RATE) for price in prices]
print("Cleaner Comprehension List for Prices", listPriceWithVAT3)

# We could use a dictionary comprehension to make if we wanted to show the original price before tax next to it
# KEY = price, VALUE = price+tax
# assigning key 'price' to value 'price * (1 + TAX_RATE) for each variable/value ('price')
# in the prices list
price_dict = {price: price * (1 + TAX_RATE) for price in prices}
print("Dictionary of Prices with VAT next to original price", price_dict)

# Example of using the walrus operator

# create function for creating random weather values in Fahrenheit
def get_weather_data():
     return random.randrange(90, 110)

# let's say you only want the tempatures greater than 100
# instead of checking if the tempature is greater than 100 and then assigning on another line you can use the walrus operator.
# the walrus operator checks if the value passes the condition and then assigns it to the variable temp
# the _ indicates to python the variable is throw away this means we dont care about it.
# we are using the _ because we do not care about iterations through the loop they aren't involved in the logic of creating entries in the list
# so 20 random variables are returned by the get_weather_data function (because range = 20).
# you are calling the get_weather_data function 20 times
# temp only becomes a value if it is greater than 100
tempList = [temp for _ in range(20) if (temp := get_weather_data()) >= 100]
print("Temp List using Walrus Operator", tempList)
