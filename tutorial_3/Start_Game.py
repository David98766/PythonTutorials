from tutorial_3.model.Rebel import Rebel
from tutorial_3.model.Soldier import Soldier
#Notice we do not have to call Character class: its is an ABSTRACT class

# Function to get user input for the character name and class selection
def choose_character():
    # Getting the player's name and converting it to uppercase within the class constructor
    name = input("Enter your character's name: ")

    # Asking the player to choose a class and converting it to uppercase
    # to ensure consistent comparisons (e.g., 'SOLDIER' and 'soldier' are treated the same).
    character_class = input("Choose your class (SOLDIER/REBEL): ").upper()

    # If the player chooses 'SOLDIER', return a SOLDIER object
    if character_class == "SOLDIER":
        return Soldier(name)
    # If the player chooses 'REBEL', return a REBEL object
    elif character_class == "REBEL":
        return Rebel(name)
    # If the player enters anything else, default to SOLDIER
    else:
        print("Invalid class choice, defaulting to SOLDIER.")
        return Soldier(name)


# Main game flow function
def start_game():
    print("Welcome to the game!")  # Welcome message

    # Call choose_character to get user input and create the player character
    player = choose_character()

    # Introduce the player character by calling the introduce method
    player.introduce()

    # Show the player's initial health using the show_health method
    player.show_health()

    # Ask the player if they want to attack and convert their response to uppercase
    action = input("Do you want to attack? (yes/no): ").upper()

    # If the player enters 'YES', call the attack method based on the character class
    if action == "YES":
        player.attack()
    # If the player enters anything else, no action is taken
    else:
        print(f"{player._name} decides to rest.")  # Player chooses not to attack


# Start the game by calling the start_game function
start_game()