#2 List Converted into Dictionary and then passed into a for loop to print the name and marks of each student
names = ["Aarav", "Diya", "Kabir"]
marks = [88, 91, 76]

student_marks = dict(zip(names, marks))
print(student_marks)
# {'Aarav': 88, 'Diya': 91, 'Kabir': 76}

for name, mark in student_marks.items():
    print(f"{name} scored {mark}")