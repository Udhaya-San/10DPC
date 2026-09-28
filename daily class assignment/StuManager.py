students = []

try:
    num_students = int(input("How many students do you want to enter? "))

    for i in range(num_students):
        print(f"\nStudent {i + 1}")

        name = input("Enter student name: ")
        marks = float(input("Enter marks (0-100): "))

        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100")

        if marks >= 90:
            grade = "A"
        elif marks >= 80:
            grade = "B"
        elif marks >= 70:
            grade = "C"
        elif marks >= 60:
            grade = "D"
        else:
            grade = "F"

        students.append({
            "name": name,
            "marks": marks,
            "grade": grade
        })

    print("\nStudent Report")
    print("-" * 30)
    print("Name\t\tMarks\tGrade")

    for student in students:
        print(
            f"{student['name']}\t\t{student['marks']}\t{student['grade']}"
        )

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Unexpected Error:", e)