n = int(input("enter the number:"))
i=1
sum=0

for i in range(1,n+1):  #add the numbers which completely divide by 5
    if i%5==0:    
        sum+=i     
print(sum)
