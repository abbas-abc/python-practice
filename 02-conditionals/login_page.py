user_name = input("username: ")
password = input("password: ")

if user_name == "admin" and password == "pass":
    print("You are successfully login")                 #we use and with addition to if and else
else:
    print("Your username or password is incorrect.")