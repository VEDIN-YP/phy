import random


questions = [
    {
        "question": "Which language is mainly used for web page structure?",
        "options": ["A. Python", "B. HTML", "C. C++", "D. Java"],
        "answer": "B"
    },

    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Personal Unit",
            "C. Central Program Utility",
            "D. Core Processing User"
        ],
        "answer": "A"
    },

    {
        "question": "Which data type stores True or False?",
        "options": [
            "A. String",
            "B. Integer",
            "C. Boolean",
            "D. Float"
        ],
        "answer": "C"
    },

    {
        "question": "Which symbol is used for comments in Python?",
        "options": [
            "A. //",
            "B. #",
            "C. <!--",
            "D. **"
        ],
        "answer": "B"
    },

    {
        "question": "Which keyword is used to create a function in Python?",
        "options": [
            "A. function",
            "B. func",
            "C. define",
            "D. def"
        ],
        "answer": "D"
    }
]


def show_question(question, number):

    print("\n" + "=" * 50)
    print(f"Question {number}")
    print("=" * 50)

    print(question["question"])

    for option in question["options"]:
        print(option)


def get_answer():

    while True:

        answer = input("\nYour answer: ").upper()

        if answer in ["A", "B", "C", "D"]:
            return answer

        print("Please enter A, B, C, or D.")


def run_quiz():

    score = 0
    lives = 3

    quiz_questions = questions.copy()
    random.shuffle(quiz_questions)

    for number, question in enumerate(quiz_questions, start=1):

        if lives == 0:
            break

        show_question(question, number)

        answer = get_answer()

        if answer == question["answer"]:
            print("\nCorrect!")
            score += 10

        else:
            print("\nWrong!")
            print("Correct answer:", question["answer"])
            lives -= 1
            print("Lives remaining:", lives)

    return score, lives


def show_result(score, lives, total_questions):

    print("\n" + "=" * 50)
    print("                 FINAL RESULT")
    print("=" * 50)

    print("Score:", score)
    print("Maximum score:", total_questions * 10)
    print("Lives remaining:", lives)

    percentage = (score / (total_questions * 10)) * 100

    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    print("Grade:", grade)

    if grade == "F":
        print("Result: FAIL")
    else:
        print("Result: PASS")


def main():

    print("=" * 50)
    print("              PYTHON QUIZ SYSTEM")
    print("=" * 50)

    print("\nRules:")
    print("- Each correct answer gives 10 points.")
    print("- You have 3 lives.")
    print("- A wrong answer removes one life.")
    print("- The quiz ends when you lose all lives.")

    input("\nPress Enter to start...")

    score, lives = run_quiz()

    show_result(
        score,
        lives,
        len(questions)
    )


main()
