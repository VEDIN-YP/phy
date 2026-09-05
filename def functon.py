students = []


def add_student():
    print("\n--- ADD STUDENT ---")

    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)

    print("Student added successfully!")


def show_students():
    print("\n--- ALL STUDENTS ---")

    if len(students) == 0:
        print("No students found.")
        return

    for i, student in enumerate(students, start=1):
        print("\nStudent", i)
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Marks:", student["marks"])


def search_student():
    print("\n--- SEARCH STUDENT ---")

    name = input("Enter student name: ")

    for student in students:

        if student["name"].lower() == name.lower():
            print("\nStudent found!")
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Marks:", student["marks"])
            return

    print("Student not found.")


def calculate_average():
    print("\n--- AVERAGE MARKS ---")

    if len(students) == 0:
        print("No students available.")
        return

    total = 0

    for student in students:
        total += student["marks"]

    average = total / len(students)

    print("Average marks:", average)


def find_top_student():
    print("\n--- TOP STUDENT ---")

    if len(students) == 0:
        print("No students available.")
        return

    top_student = students[0]

    for student in students:

        if student["marks"] > top_student["marks"]:
            top_student = student

    print("Top student:", top_student["name"])
    print("Marks:", top_student["marks"])


def delete_student():
    print("\n--- DELETE STUDENT ---")

    name = input("Enter student name: ")

    for student in students:

        if student["name"].lower() == name.lower():

            students.remove(student)

            print("Student deleted successfully!")
            return

    print("Student not found.")


def menu():

    while True:

        print("\n==============================")
        print("     STUDENT MANAGEMENT")
        print("==============================")

        print("1. Add student")
        print("2. Show students")
        print("3. Search student")
        print("4. Calculate average")
        print("5. Find top student")
        print("6. Delete student")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            show_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            calculate_average()

        elif choice == "5":
            find_top_student()

        elif choice == "6":
            delete_student()

        elif choice == "7":
            print("Program closed.")
            break

        else:
            print("Invalid choice!")


menu()

