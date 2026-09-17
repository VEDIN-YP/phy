# Student Tuple Program

student = ("Rahul", 16, "Class 11", 85, 78, 92)

print("Student Details")
print("----------------")

print("Name:", student[0])
print("Age:", student[1])
print("Class:", student[2])

print("\nMarks:")
print("English:", student[3])
print("Maths:", student[4])
print("Science:", student[5])

# Calculate total marks
total = student[3] + student[4] + student[5]

# Calculate percentage
percentage = total / 3

print("\nTotal Marks:", total)
print("Percentage:", percentage)

# Check result
if percentage >= 80:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 40:
    print("Grade: C")
else:
    print("Fail")

# Display all tuple values
print("\nComplete Tuple:")

for value in student:
    print(value) 
