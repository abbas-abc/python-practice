#print only odd numbers
i=1
while (i<=10):
    if i % 2==0:
        i+=1
        continue
    print(i)
    i+=1
print("outside the loop....")