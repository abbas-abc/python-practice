def si(principle,rate,time):
    return (principle*rate*time)/100

principle= float(input("P: ")) 
rate = float(input("R: "))
time = float(input("T: "))  

print(si(principle, rate, time))