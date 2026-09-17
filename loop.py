# Infinite Loop Menu Program

while True:

    print("\n======================")
    print("     MAIN MENU")
    print("======================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Check Even or Odd")
    print("6. Multiplication Table")
    print("7. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        print("Addition =", a + b)

    elif choice == 2:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        print("Subtraction =", a - b)

    elif choice == 3:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        print("Multiplication =", a * b)

    elif choice == 4:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if b != 0:
            print("Division =", a / b)
        else:
            print("Cannot divide by zero!")

    elif choice == 5:
        num = int(input("Enter a number: "))

        if num % 2 == 0:
            print(num, "is EVEN")
        else:
            print(num, "is ODD")

    elif choice == 6:
        num = int(input("Enter a number: "))

        print("\nMultiplication Table of", num)

        for i in range(1, 11):
            print(num, "x", i, "=", num * i)

    elif choice == 7:
        print("Program Ended!")
        break

    else:
        print("Invalid choice! Please try again.")
        
