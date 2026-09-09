set1 = {1, 2, 3, 2, 4, 5}
set2 = {1, 5}

print(set1)         #not print the duplicate

set1.add(6)  #it add the new element to set
print(set1)         

set1.remove(6)      #this remove the exesting element of the set
print(set1)          

print(set1.union(set2)) #it will take the union b/w sets(print all elements of both)
        
print(set1.intersection(set2))  # it will print pnly the common elements b/w both sets

set1.clear()  #it make the set empty 
print(set1)          