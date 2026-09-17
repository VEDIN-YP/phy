# Indexing and Slicing Program

numbers = (10, 20, 30, 40, 50, 60, 70, 80)

print("Original Tuple:", numbers)

# INDEXING
print("\n--- Indexing ---")

print("First element:", numbers[0])
print("Third element:", numbers[2])
print("Fifth element:", numbers[4])
print("Last element:", numbers[-1])
print("Second last element:", numbers[-2])

# SLICING
print("\n--- Slicing ---")

print("First 4 elements:", numbers[0:4])
print("Elements from index 2 to 5:", numbers[2:6])
print("From index 3 to end:", numbers[3:])
print("First 5 elements:", numbers[:5])
print("Every second element:", numbers[::2])
print("Reverse tuple:", numbers[::-1])
