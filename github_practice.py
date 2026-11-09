# Student Performance Analyzer
# Git and GitHub Practice Project

students = {
    "Umair": 85,
    "Ali": 72,
    "Ahmed": 91,
    "Hassan": 65,
    "Usman": 78
}

print("Student Performance Analyzer")
print("-" * 35)

for name, marks in students.items():

    if marks >= 80:
        grade = "A"

    elif marks >= 70:
        grade = "B"

    elif marks >= 60:
        grade = "C"

    else:
        grade = "F"

    print(f"{name}: {marks} marks | Grade: {grade}")

average_marks = sum(students.values()) / len(students)

print("-" * 35)
print(f"Class Average: {average_marks:.2f}")