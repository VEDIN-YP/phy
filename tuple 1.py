# Creating a tuple
numbers = (10, 20, 30, 40, 50, 60, 70)

print("Original Tuple:", numbers)

# Accessing tuple elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Length of tuple
print("Number of elements:", len(numbers))

# Maximum and minimum
print("Largest number:", max(numbers))
print("Smallest number:", min(numbers))

# Sum of elements
print("Sum:", sum(numbers))

# Slicing
print("First 4 elements:", numbers[0:4])
print("Last 3 elements:", numbers[-3:])

# Checking an element
num = int(input("Enter a number to search: "))

if num in numbers:
    print(num, "is present in the tuple")
else:
    print(num, "is not present in the tuple")

# Loop through tuple
print("\nAll tuple elements:")

for x in numbers:
    print(x)
