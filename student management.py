import json

FILE_NAME = "students.json"


def load_students():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student(students):
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    marks = {}

    subjects = ["English", "Computer Science", "Economics", "Accountancy"]

    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks in {subject}: "))

                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    students.append(student)
    save_students(students)

    print("\nStudent added successfully.")


def calculate_percentage(marks):
    total = sum(marks.values())
    return total / len(marks)


def display_students(students):

    if not students:
        print("\nNo students found.")
        return

    print("\n========== STUDENTS ==========")

    for student in students:

        percentage = calculate_percentage(student["marks"])

        print("\nName:", student["name"])
        print("Roll:", student["roll"])

        for subject, mark in student["marks"].items():
            print(f"{subject}: {mark}")

        print(f"Percentage: {percentage:.2f}%")


def search_student(students):

    roll = input("Enter roll number to search: ")

    for student in students:

        if student["roll"] == roll:

            print("\nStudent Found")
            print("----------------")
            print("Name:", student["name"])
            print("Roll:", student["roll"])

            percentage = calculate_percentage(student["marks"])

            for subject, mark in student["marks"].items():
                print(f"{subject}: {mark}")

            print(f"Percentage: {percentage:.2f}%")

            return

    print("Student not found.")


def show_topper(students):

    if not students:
        print("No students available.")
        return

    topper = max(
        students,
        key=lambda student: calculate_percentage(student["marks"])
    )

    percentage = calculate_percentage(topper["marks"])

    print("\n========== TOPPER ==========")
    print("Name:", topper["name"])
    print("Roll:", topper["roll"])
    print(f"Percentage: {percentage:.2f}%")


def sort_students(students):

    sorted_students = sorted(
        students,
        key=lambda student: calculate_percentage(student["marks"]),
        reverse=True
    )

    print("\n===== RANKING =====")

    for rank, student in enumerate(sorted_students, start=1):

        percentage = calculate_percentage(student["marks"])

        print(
            f"{rank}. {student['name']} "
            f"({percentage:.2f}%)"
        )


def main():

    students = load_students()

    while True:

        print("\n==============================")
        print("   STUDENT MANAGEMENT SYSTEM")
        print("==============================")

        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Show Topper")
        print("5. Show Ranking")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            display_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            show_topper(students)

        elif choice == "5":
            sort_students(students)

        elif choice == "6":
            print("Program closed.")
            break

        else:
            print("Invalid choice. Try again.")


main()
