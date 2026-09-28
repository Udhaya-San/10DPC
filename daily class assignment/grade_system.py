students = []

try:
    while True:
        try:
            num_students = int(input("How many students do you want to enter? "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        if num_students <= 0:
            print("Please enter a number greater than 0.")
            continue

        break

    for i in range(num_students):
        print(f"\nStudent {i + 1}")

        while True:
            name = input("Enter student name: ")

            if name.isalpha():
                break

            print("Invalid name! Please enter alphabets only.")
        while True:
            try:
                marks = float(input("Enter marks (0-100): "))

                if 0 <= marks <= 100:
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Invalid input! Please enter a numeric value.")

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