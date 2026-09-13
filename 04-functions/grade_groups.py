def grade_groups(scores):
    passed=[]
    fails=[]
    for names,marks in scores.items():
        if marks>=60:
            passed.append(names)
        else:
            fails.append(names)
    return(passed,fails)

scores = {"Ali": 85, "Sara": 45, "Omar": 92, "Bob": 38}
passed, fails = grade_groups(scores)
print(passed)   
print(fails)   