class Character:
    def __init__(self, name):
        # The constructor initializes the character's name and health.
        # In Python putting an underscore at the start of a variable makes it a PRIVATE variable (Encapsulation)
        # Using upper() method to convert the player's name to uppercase.
        self._name = name.upper()
        self._health = 100

    # Abstraction: Simplified interface to introduce the character.
    def introduce(self):
        # an f string allows you to embed a variable directly into the string.
        print(f"Welcome, {self._name}!")

    # Method to display the character's health to the user.
    def show_health(self):
        print(f"{self._name}'s health: {self._health}")

    # Polymorphism: The attack method will be defined differently for each subclass.
    # Here it's just a placeholder to be overridden by subclasses (Soldier, Rebel).
    def attack(self):
        #PLACEHOLDER:
        pass