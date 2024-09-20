from tutorial_3.model.Character import Character

# Inheritance: Soldier class inherits from Character
class Soldier(Character):
    def __init__(self, name):
        # Calling the parent (Character) class constructor using super()
        super().__init__(name)

    # Polymorphism: Soldier has its own version of the attack method
    # which is different from the other subclasses.
    def attack(self):
        print(f"{self._name} Fires at the enemy!")