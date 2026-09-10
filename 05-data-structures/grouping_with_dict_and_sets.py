info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]

# Q1: Find all unique courses being offered (no duplicates)
unique_courses = set()
for names, courses in info:
    unique_courses.add(courses)
print(unique_courses)


# Q2: Find the names of everyone taking English
for names, courses in info:
    if courses == "English":
        print(names)


# Q3: Group each person with the set of all courses they're taking
dict = {}
for names, courses in info:
    if dict.get(names) == None:
        dict.update({names: set()})
        dict[names].add(courses)
    else:
        dict[names].add(courses)
print(dict)
