P1 = {
    "Name":"Udhaya Sankar",
    "Age": 38,
    "Relationship": "Father"
}
P2 = {
    "Name":"Devipriya",
    "Age": 35,
    "Relationship": "Mother"
}
P3 ={
    "Name":"Prithoon",
    "Age": 11,
    "Relationship": "Son"
}
P4 ={
    "Name":"Prithvik",
    "Age": 7,
    "Relationship": "Second Son"
}
Family= [P1, P2, P3, P4]
print(Family)

for Person in Family:
    print(Person)
    
from tabulate import tabulate # type: ignore
print(tabulate(Family, headers="keys", tablefmt="grid"))