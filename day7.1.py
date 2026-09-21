def get_common_skills(skilset, required):
    frozen_skillset = frozenset(skilset)
    frozen_required = frozenset(required)
    return frozen_skillset & frozen_required

skilset = {"Git", "Python", "JavaScript", "HTML", "CSS", "SQL", "Django", "Flask", "React", "Node.js"}
required = {"Python", "JavaScript", "SQL", "Django", "Flask"}

common = get_common_skills(skilset, required)

# looping over a frozenset (read-only iteration)
print("Common skills:")
for skill in common:
    print("-", skill)

# building a frozenset via a loop: collect into a regular set first, then freeze
temp = set()
for skill in skilset:
    if skill.startswith("J") or skill.startswith("P"):
        temp.add(skill)
filtered = frozenset(temp)
print("Filtered:", filtered)