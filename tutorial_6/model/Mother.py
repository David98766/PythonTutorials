class Mother:
    def __init__(self, name, address, age, ssn):
        self.name = name
        self.address = address
        self.age = age
        self.ssn = ssn
        self.pregnancy_details = []

    def add_pregnancy(self, pregnancy):
        self.pregnancy_details.append(pregnancy)