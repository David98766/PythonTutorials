from Tutorial2.model.Crisp import Crisp
from Tutorial2.converter.ConvertToCurrency import convertNumberToPrice

# this class is 3rd level of inheritance the grandparent is Product and direct parent Crisp class
class Tayto(Crisp):
    #so it inherits all its characteristics from both product and Crisp class
    def __init__(self, name, price, grams):
        super().__init__(name, price, grams)

    # overriding method for getPrice method from parent Crisp and adding unique implementation for Tayto object
    def getPrice(self):
        print("The ", self.grams, "g bag of " + self.name + " costs: €", convertNumberToPrice(self.price), sep = "")


