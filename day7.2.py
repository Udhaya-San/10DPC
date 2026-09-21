skilset = {"Git", "Python", "JavaScript", "HTML", "CSS", "SQL", "Django", "Flask", "React", "Node.js"}
required = {"Python", "JavaScript", "SQL", "Django", "Flask"}
extra = {"Python", "Kubernetes"}

print("Skill Set:", skilset)
for skill in skilset:
    print(" -", skill)

print("\nRequired Skills:", required)

# --- combining operators (return a new set) ---
print("\nUnion (|):            ", skilset | required)
print("Intersection (&):     ", skilset & required)
print("Difference (-):       ", skilset - required)
print("Symmetric diff (^):   ", skilset ^ required)

# --- comparison operators (return a bool) ---
print("\nSubset (<=):          ", required <= skilset)
print("Proper subset (<):    ", required < skilset)
print("Superset (>=):        ", skilset >= required)
print("Proper superset (>):  ", skilset > required)
print("Equal (==):           ", skilset == required)
print("Not equal (!=):       ", skilset != required)
print("Disjoint:             ", skilset.isdisjoint({"Go", "Rust"}))

# --- in-place operators (mutate the left set) ---
s = set(skilset)
s |= extra
print("\nAfter |= extra:       ", s)

s = set(skilset)
s &= required
print("After &= required:    ", s)

s = set(skilset)
s -= required
print("After -= required:    ", s)

s = set(skilset)
s ^= extra
print("After ^= extra:       ", s)

# --- frozenset: immutable version built via a function/loop ---
def get_common_skills(a, b):
    frozen_a = frozenset(a)
    frozen_b = frozenset(b)
    return frozen_a & frozen_b

common = get_common_skills(skilset, required)
print("\nCommon skills (frozenset):", common)
for skill in common:
    print(" -", skill)

try:
    common.add("Go")
except AttributeError as e:
    print("\nCannot modify frozenset ->", e)