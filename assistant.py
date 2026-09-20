import datetime
import random
import math
import time


# -----------------------------
# AI PERSONAL ASSISTANT
# -----------------------------

name = input("Enter your name: ")

print("\nInitializing assistant...")
time.sleep(1)

print("Loading modules...")
time.sleep(1)

print("System ready.")

while True:

    print("\n" + "=" * 50)
    print("              PYTHON AI ASSISTANT")
    print("=" * 50)

    print("""
1. Ask the time
2. Ask the date
3. Calculator
4. Number guessing game
5. Generate random number
6. Math tools
7. Motivational message
8. System status
9. Exit
""")

    choice = input("Choose an option: ")

    # TIME
    if choice == "1":

        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        print("\nCurrent time:", current_time)

    # DATE
    elif choice == "2":

        today = datetime.datetime.now()

        print("\nDate:", today.strftime("%d-%m-%Y"))
        print("Day:", today.strftime("%A"))

    # CALCULATOR
    elif choice == "3":

        print("\n--- Calculator ---")

        a = float(input("Enter first number: "))
        operator = input("Enter operator (+ - * /): ")
        b = float(input("Enter second number: "))

        if operator == "+":
            result = a + b

        elif operator == "-":
            result = a - b

        elif operator == "*":
            result = a * b

        elif operator == "/":

            if b == 0:
                print("Cannot divide by zero.")
                continue

            result = a / b

        else:
            print("Invalid operator.")
            continue

        print("Result:", result)

    # GUESSING GAME
    elif choice == "4":

        secret = random.randint(1, 100)
        attempts = 0

        print("\nI have selected a number between 1 and 100.")

        while True:

            guess = int(input("Your guess: "))
            attempts += 1

            if guess < secret:
                print("Too low.")

            elif guess > secret:
                print("Too high.")

            else:
                print("\nCorrect!")
                print("Attempts:", attempts)
                break

    # RANDOM NUMBER
    elif choice == "5":

        minimum = int(input("Minimum number: "))
        maximum = int(input("Maximum number: "))

        number = random.randint(minimum, maximum)

        print("\nGenerated number:", number)

    # MATH TOOLS
    elif choice == "6":

        print("""
1. Square root
2. Power
3. Factorial
""")

        option = input("Choose: ")

        if option == "1":

            number = float(input("Enter number: "))

            if number < 0:
                print("Cannot calculate square root of a negative number.")
            else:
                print("Square root:", math.sqrt(number))

        elif option == "2":

            number = float(input("Enter number: "))
            power = float(input("Enter power: "))

            print("Answer:", math.pow(number, power))

        elif option == "3":

            number = int(input("Enter a positive integer: "))

            if number < 0:
                print("Invalid number.")
            else:
                print("Factorial:", math.factorial(number))

        else:
            print("Invalid option.")

    # MOTIVATION
    elif choice == "7":

        messages = [
            "Keep going. Progress takes time.",
            "Small improvements become big results.",
            "Consistency beats motivation.",
            "Learn something new every day.",
            "Don't quit just because something is difficult."
        ]

        print("\nAI Message:")
        print(random.choice(messages))

    # SYSTEM STATUS
    elif choice == "8":

        print("\nChecking system...")

        time.sleep(1)

        print("""
---------------------------------
SYSTEM STATUS
---------------------------------
Assistant      : ONLINE
Python Engine  : ACTIVE
Math Module    : READY
Random Module  : READY
Time Module    : READY
---------------------------------
User           : """ + name + """
Status         : CONNECTED
---------------------------------
""")

    # EXIT
    elif choice == "9":

        print("\nShutting down assistant...")

        time.sleep(1)

        print("Goodbye,", name)

        break

    else:

        print("\nInvalid choice. Try again.")
