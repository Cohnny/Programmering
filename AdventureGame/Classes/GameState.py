class GameState:
    # Different game states
    MAIN_MENU = "Main Menu"
    EXPLORATION = "Exploration"
    CHALLENGE = "Challenge"
    GAME_OVER = "Game Over"

    # TODO Create a challenge class which holds all the information
    challenges = {
        "Troll": {
            "Description": {
                "1": ("As you venture deeper into the forest, a menacing presence looms before you."
                      "A massive, moss-covered troll steps out from behind a towering oak tree. "
                      "Its yellow eyes fixate on you with a hungry gleam, and its hulking form casts"
                      "a long shadow across your path. Beads of saliva glisten on its jagged,"
                      "yellow teeth as it lets out a bone-chilling growl. Brace yourself for a battle,"
                      "for you've crossed paths with a formidable forest troll!"),
                "2": ("As you trudge through the murky swamp, the ground trembles beneath your feet."
                      "A monstrous figure emerges from the mists, towering over the twisted trees."
                      "It's a troll, its warty, green flesh dripping with slimy swamp water."
                      "Its bulbous eyes, glowing with malevolence, lock onto you."
                      "The stench of decay and algae fills the air as it raises a colossal,"
                      "club-like arm, ready to strike. You've stumbled upon a fearsome swamp troll,"
                      "and a perilous battle awaits."),
                "3": ("As you navigate the dense, shadowy depths of the primeval forest,"
                      "an ominous rustling of leaves and snapping of branches fills the air."
                      "Suddenly, a monstrous figure steps into your path, blocking out the dappled sunlight."
                      "It's a troll, its gnarled, mossy skin blending seamlessly with the surrounding foliage."
                      "Its eyes, gleaming with cunning, lock onto you with a predatory focus."
                      "The eerie hush of the forest is shattered by the troll's guttural growl"
                      "as it brandishes a wickedly barbed club, entangled with thorny vines."
                      "You've stumbled upon a formidable forest troll, a guardian of these dark woods,"
                      "and a battle in this untamed realm is inevitable.")
            }
        }
    }

    # Constructor
    def __init__(self):
        self.current_state = self.MAIN_MENU

    # Handles main menu state
    def handle_main_menu(self):
        print("Welcome to the Text Adventure Game!")
        print("1. Start Game")
        print("2. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("You start the game.")
            self.current_state = self.EXPLORATION
        elif choice == "2":
            print("Goodbye!")
            self.current_state = self.GAME_OVER
        else:
            print("Invalid choice. Please try again.")

    # Handles the exploration state
    def handle_exploration(self):
        print("SOME KIND OF WELCOME MESSAGE")  # TODO Implement welcome message (with greetings to the player name)
        print("MORE WELCOME MESSAGE IF NEEDED")
        print("1. FIRST CHOICE")  # TODO Think of implementing some randomness into the exploration
        print("2. SECOND CHOICE")
        choice = input("Enter your choice: ")

        if choice == "1":  # TODO Placeholder just for checking functions/choices
            self.current_state = self.CHALLENGE
            self.handle_challenge("max_hp")
        elif choice == "2":  # TODO Placeholder just for checking functions/choices
            self.current_state = self.CHALLENGE
            self.handle_challenge("damage")
        else:
            print("Invalid choice. Please try again.")

    # Handles the challenge state
    def handle_challenge(self, challenge_type):
        if challenge_type == "max_hp":
            print("Max HP challenge")
            self.current_state = self.GAME_OVER
        elif challenge_type == "damage":
            print("Damage challenge")
            self.current_state = self.GAME_OVER
