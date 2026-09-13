def grade_categories(scores):
    grades = {"A": [], "B": [], "C": [], "F": []}
    for names,marks in scores.items():
        if marks>=90:
            grades["A"].append(names)
        elif marks>=75 and marks<90:
            grades["B"].append(names)
        elif marks>=60 and marks<75:
            grades["C"].append(names)
        else:
            grades["F"].append(names)
    return(grades)
scores = {"Ali": 85, "Sara": 45, "Omar": 92, "Bob": 38, "Zara": 68}
result = grade_categories(scores)
print(result)