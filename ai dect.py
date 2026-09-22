print("=" * 60)
print("                 THE LOST CITY")
print("=" * 60)

player = input("\nEnter your name: ")

health = 100
coins = 20
inventory = []

print(f"\nWelcome, {player}.")
print("You wake up near an abandoned city.")
print("There are three paths in front of you.")

while health > 0:

    print("\n----------------------------------------")
    print(f"Health: {health} | Coins: {coins}")
    print("Inventory:", inventory if inventory else "Empty")
    print("----------------------------------------")

    print("\n1. Enter the forest")
    print("2. Enter the old building")
    print("3. Visit the market")
    print("4. Check inventory")
    print("5. Quit")

    choice = input("\nChoose: ")

    if choice == "1":

        print("\nYou enter the forest...")

        event = (health + coins) % 3

        if event == 0:
            print("You find a hidden treasure.")
            coins += 30

        elif event == 1:
            print("You find a health potion.")
            inventory.append("Health Potion")

        else:
            print("You get lost and lose some health.")
            health -= 15

    elif choice == "2":

        print("\nYou enter the abandoned building.")

        if "Key" in inventory:

            print("You use the Key to open a secret room.")
            print("You discover 100 coins!")
            coins += 100

        else:

            print("A locked door blocks your way.")
            print("You search the building...")

            search = input("Search for the key? (yes/no): ")

            if search.lower() == "yes":

                if coins % 2 == 0:
                    print("You found a Key!")
                    inventory.append("Key")
                else:
                    print("You couldn't find anything.")

    elif choice == "3":

        print("\nMARKET")
        print("1. Buy Health Potion - 15 coins")
        print("2. Buy Key - 25 coins")
        print("3. Leave")

        buy = input("Choose: ")

        if buy == "1":

            if coins >= 15:
                coins -= 15
                inventory.append("Health Potion")
                print("Health Potion purchased.")
            else:
                print("Not enough coins.")

        elif buy == "2":

            if coins >= 25:
                coins -= 25
                inventory.append("Key")
                print("Key purchased.")
            else:
                print("Not enough coins.")

    elif choice == "4":

        print("\nYOUR INVENTORY")

        if inventory:
            for item in inventory:
                print("-", item)
        else:
            print("Your inventory is empty.")

    elif choice == "5":

        print("\nYou leave the city.")
        print(f"Final coins: {coins}")
        print(f"Final health: {health}")
        break

    else:
        print("Invalid choice.")

    # Automatically use potion if health gets low
    if health <= 40 and "Health Potion" in inventory:

        use = input("\nYour health is low. Use a Health Potion? (yes/no): ")

        if use.lower() == "yes":

            health += 30
            inventory.remove("Health Potion")

            if health > 100:
                health = 100

            print("Health restored!")

if health <= 0:
    print("\nGAME OVER")
    print("You ran out of health.")

print("\nThanks for playing.")
