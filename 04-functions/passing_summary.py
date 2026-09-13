def passing_summary(scores):
    count=0
    passing=[]
    for names,marks in scores.items():
        if marks>=60:
            passing.append(names)
            count+=1
    return(passing,count)
scores = {"Ali": 85, "Sara": 45, "Omar": 92, "Bob": 38}
names, count = passing_summary(scores)

print(names)
print(count)
