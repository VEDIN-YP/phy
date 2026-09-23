print("=" * 50)
print("          NUMBER PATTERN ANALYZER")
print("=" * 50)

numbers = []

n = int(input("\nHow many numbers do you want to enter? "))

for i in range(n):
    value = int(input(f"Enter number {i + 1}: "))
    numbers.append(value)

print("\nNumbers:", numbers)

# Find increasing/decreasing pattern
increasing = True
decreasing = True

for i in range(1, len(numbers)):

    if numbers[i] <= numbers[i - 1]:
        increasing = False

    if numbers[i] >= numbers[i - 1]:
        decreasing = False

print("\n========== ANALYSIS ==========")

if increasing:
    print("Pattern: Strictly Increasing")

elif decreasing:
    print("Pattern: Strictly Decreasing")

else:
    print("Pattern: Mixed")

# Even and odd numbers
even = []
odd = []

for number in numbers:

    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print("Even numbers:", even)
print("Odd numbers :", odd)

# Largest and smallest
print("Largest     :", max(numbers))
print("Smallest    :", min(numbers))

# Difference between first and last
difference = numbers[-1] - numbers[0]

print("First number:", numbers[0])
print("Last number :", numbers[-1])
print("Difference  :", difference)

print("==============================")
