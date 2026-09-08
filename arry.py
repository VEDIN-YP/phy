numbers = []

print("Enter 5 numbers:")

for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)

print("Numbers are:", numbers)
print("Sum =", sum(numbers))
print("Largest =", max(numbers))
print("Smallest =", min(numbers))
