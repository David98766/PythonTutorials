from Tutorial2.model.Crisp import Crisp
from Tutorial2.converter.ConvertToCurrency import convertNumberToPrice

class Tayto(Crisp):
    def __init__(self, name, price, grams):
        super().__init__(name, price, grams)

    def getPrice(self):
        print("The ", self.grams, "g bag of " + self.name + " costs: €", convertNumberToPrice(self.price), sep = "")


