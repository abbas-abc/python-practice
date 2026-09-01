
def greet_user(name):           #through dep() we can make custom functions
    print("Welcome,", name+"!" " Let's learn Python.")
greet_user("Afaq")         #we can reuse that functions with writng it over and over
greet_user("Abbas")    


#return
def cube(number):
    return number**3
result = cube(2)
print("Cube of 2 is", result )