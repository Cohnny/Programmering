description = ("You find yourself in a big room with a chandeler hanging from the roof."
               "There are paintings hanging on the walls.")
doors = ["north", "south", "east", "west"]


# Welcome screen
def welcome():
    directions = ""

    print("Hi and welcome to this adventure game")
    print("-------------------------------------")
    print()
    print(description)
    print(f"When you look around you see doors to your:")
    for direction in doors:
        directions = directions + direction + ", "
    print(directions)
    print()


# Menu
def menu():
    print("What do you want to do?")
    print("1. Go north")
    print("2. Go south")
    print("3. Go east")
    print("4. Go west")
    print("5. Look")
    print("6. Quit game")
    print()


# Main loop
def main():
    welcome()

    run = True
    while run:
        menu()
        choice = input("Enter your choice: ")

        if not choice.isnumeric():
            print("Wrong input. Please enter a number (1-6)")
            continue

        choice = int(choice)
        if choice == 6:
            run = False


# Initialize
if __name__ == "__main__":
    main()