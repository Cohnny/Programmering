import random

from DataManager import load_data
from .Player import Player
from .Enemy import Enemy


class GameState:
    # Different game states
    MAIN_MENU = "Main Menu"
    EXPLORATION = "Exploration"
    COMBAT = "Combat"
    CHALLENGE = "Challenge"
    GAME_OVER = "Game Over"

    # Constructor. Sets state, creates player object, loads JSON data.
    def __init__(self):
        self.state = self.MAIN_MENU
        self.player = Player("", 100, 10)
        self.data = load_data("Data/Events.json")

    # Handles main menu state
    def handle_main_menu(self):
        name = input("Hello adventurer what's your name?: ")
        self.player.set_player_name(name)
        print()
        print(f"Welcome to Gloomhaven, {self.player.name}. The air is thick with mystery and danger in these shadowed\n"
              f"streets. Prepare yourself, for the path ahead is treacherous, and the denizens of Murkwood are not to\n"
              f"be trifled with. Your fate awaits, brave traveler.")
        print()
        print("Begin your journey or take farewell: ")
        print("1. Start Game")
        print("2. Quit")

        choice = input("Enter your choice: ")
        print()

        if choice == "1":
            self.state = self.EXPLORATION
        elif choice == "2":
            print("Farewell!")
            self.state = self.GAME_OVER
        else:
            print("Invalid choice. Please try again.")

    # Handles the exploration state.
    def handle_exploration(self):
        print("As you step forward into the unknown, you bid farewell to the gloomy streets of Gloomhaven and step\n"
              "deeper into the heart of Murkwood. Here, the air is heavy with an eerie mist, and the ancient trees\n"
              "stretch their gnarled branches towards the sky, casting long, ominous shadows. Mysterious noises drift\n"
              "through the dense forest, hinting at the challenges awaiting you in this enigmatic realm. Murkwood is\n"
              "a place where your bravery and cunning will be put to the test, as you seek to unveil the hidden\n"
              "mysteries that lie within. Your adventure begins now.")
        print("1. Go left")
        print("2. Go right")
        choice = input("Enter your choice: ")
        print()

        # Gets a random enemy from dictionary. Creates an enemy object and sets its name, damage and hp.
        # Calls and print the enemy to_string to show enemy info
        if choice == "1":
            random_enemy = random.choice(list(self.data.keys()))
            random_description = random.choice(list(self.data[random_enemy]["description"].values()))
            print(random_description)
            enemy = Enemy(random_enemy, self.data[random_enemy]["damage"], self.data[random_enemy]["hp"])
            enemy.to_string()
            print()
            self.handle_combat()
        # Just a placeholder. Does the same as choice 1.
        elif choice == "2":
            random_enemy = random.choice(list(self.data.keys()))
            print(type(random_enemy))
            enemy = Enemy(random_enemy, self.data[random_enemy]["damage"], self.data[random_enemy]["hp"])
            enemy.to_string()
            print()
            print()
            self.handle_combat()
        else:
            print("Invalid choice. Please try again.")

    def handle_combat(self): # TODO Add logic for combat
        self.state = self.COMBAT
        print("Ze combat not implemented. GAME OVER")
        self.state = self.GAME_OVER
