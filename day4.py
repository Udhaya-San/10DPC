#Dictionary Passed via for loop to print the name and marks of each student
student_marks = {"Aarav": 88, "Diya": 91, "Kabir": 76}

# both key and value
for name, marks in student_marks.items():
    print(f"{name} scored {marks}")

# keys only (looping over a dict directly does this by default)
for name in student_marks:
    print(name)

# values only
for marks in student_marks.values():
    print(marks)