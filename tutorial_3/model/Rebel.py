from tutorial_3.model.Character import Character

# Inheritance: Rebel class inherits from Character
class Rebel(Character):
    def __init__(self, name):
        # Calling the parent (Character) class constructor using super()
        super().__init__(name)

    # Polymorphism: Rebel has its own version of the attack method
    # which is different from Soldier's attack method.
    def attack(self):
        print(f"{self._name} Throws molotov!")