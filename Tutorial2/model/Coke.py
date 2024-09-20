from Tutorial2.model.Drink import Drink
from Tutorial2.converter.ConvertToCurrency import  convertNumberToPrice

class Coke(Drink):
    def __init__(self, name, price, millilitres):
        super().__init__(name, price, millilitres)

    def getPrice(self):
        print("The ", self.millilitres, "ml bottle of " + self.name + " costs: €", convertNumberToPrice(self.price), sep = "")


