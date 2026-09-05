def show_intro():
    print("================================")
    print("       THE DARK FOREST 🌲")
    print("================================")
    print("You are standing in a dark forest.")
    print("There are two paths in front of you.")
    print("")


def choose_path():
    choice = input("Choose a path (left/right): ").lower()

    if choice == "left":
        return "left"

    elif choice == "right":
        return "right"

    else:
        print("Invalid choice!")
        return choose_path()


def left_path():
    print("\nYou walk down the left path...")
    print("You find a mysterious chest! 📦")

    choice = input("Open it? (yes/no): ").lower()

    if choice == "yes":
        print("\n💰 You found 100 gold!")
    else:
        print("\nYou leave the chest and continue walking...")


def right_path():
    print("\nYou walk down the right path...")
    print("Suddenly, a wolf appears! 🐺")

    choice = input("Fight or run? ").lower()

    if choice == "fight":
        print("\n⚔️ You defeated the wolf!")
    elif choice == "run":
        print("\n🏃 You escaped!")
    else:
        print("\nThe wolf attacks you! 😭")


def main():
    show_intro()

    path = choose_path()

    if path == "left":
        left_path()

    elif path == "right":
        right_path()

    print("\n===== GAME OVER =====")


main()
