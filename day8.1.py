def calc(a,b):
    return a+b, a-b, a*b, a/b, a%b

print(f"Addition: {calc(10,5)[0]}")
print(f"Subtraction: {calc(10,5)[1]}")
print(f"Multiplication: {calc(10,5)[2]}")
print(f"Division: {calc(10,5)[3]}")
print(f"Modulus: {calc(10,5)[4]}")