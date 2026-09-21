skilset = {"Git", "Python", "JavaScript", "HTML", "CSS", "SQL", "Django", "Flask", "React", "Node.js"}

for skill in skilset:
    print(skill)

required = {"Python", "JavaScript", "SQL", "Django", "Flask","C++", "C#", "Java"}
for skill in required:
    print(skill)
    
common = skilset & required  # intersection, not union — and use skilset, not the loop leftover

print("Common skills:", common)

difference = required - skilset  # difference, not union — and use skilset, not the loop leftover

print("Skills in required but not in skilset:", difference)

frozen = frozenset(skilset)  # create a frozenset from the original set

print("Frozen set:", frozen)