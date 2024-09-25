from Tutorial2.model.Drink import Drink
from Tutorial2.converter.ConvertToCurrency import  convertNumberToPrice
# this class is 3rd level of inheritance the grandparent is Product and direct parent drink class
class Coke(Drink):
    #so it inherits all its characteristics from both product and drink class
    def __init__(self, name, price, millilitres):
        super().__init__(name, price, millilitres)

    # overriding method for getPrice method from parent drink and adding unique implementation for coke object
    def getPrice(self):
        print("The ", self.millilitres, "ml bottle of " + self.name + " costs: €", convertNumberToPrice(self.price), sep = "")


