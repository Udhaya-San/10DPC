age = 25

print(age > 18 and age < 60)    # both must be true
print(age < 10 or age > 18)     # any one true is enough
print(not(age > 18))            # reverses True to False


name = "Alice"
age = 22
if name == "Alice" and age > 25:
    print("Welcome, Alice!")
else:
    print("Access denied.")
   
#INTEGER EXAMPLE 
age = 25
count = 100
temperature = -5

print(type(age))

#FLOAT EXAMPLE
price = 99.99
height = 178.5
pi = 3.14159

print(type(price))

#STRING EXAMPLE
name = "Udhaya Sankar"
city = 'Chennai'
message = "Hello World"

print(type(name))

#DOUBLE EXAMPLE
salary = 50000.75

print(type(salary))

#BOOLEAN EXAMPLE
is_logged_in = True
has_permission = False

print(type(is_logged_in))


#TYPE CONVERSION EXAMPLE
age = "34"
converted_age = int(age)  # Convert string to integer
print(converted_age)  # Output: <class 'int'>

#LIST EXAMPLE
fruits = ["apple", "banana", "mango", "apple"]

print(fruits)
print(fruits[1])  # banana

fruits.append("orange")
print(fruits)

#SET EXAMPLE
fruits1 = {"apple", "banana", "mango", "apple"}

print(fruits1)

fruits1.add("orange")
print(fruits1)

#TUPLE EXAMPLE
colors = ("red", "green", "blue", "red")

print(colors)
print(colors[2])

#DICTIONARY EXAMPLE
employee = {
    "name": "Udhaya",
    "age": 35,
    "city": "Chennai"
}

print(employee)
print(employee["name"])
print(employee["age"])

#if-else example
age = 16
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
    
#IF-ELIF-ELSE example
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")
    
#Nested if-else example
experience = 6
rating = 4.5

if experience >= 5:
    if rating >= 4:
        print("Eligible for Bonus")
    else:
        print("Performance Rating Too Low")
else:
    print("Insufficient Experience")
    
    
#Error Handling Example
try:
    file = open("marks.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found!")
else:
    print("File read successfully:", data)   # runs only if NO error
finally:
    print("Program finished.")               # ALWAYS runs
    
#FILE MODES
with open("myfile.txt", "w") as file:
    file.write("Hello, this is my first file.\n")
    file.write("Python file handling is easy.")

print("File written successfully!")