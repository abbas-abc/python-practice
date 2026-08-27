#strip removes extra spaces from output
name = input("What is your name? ").strip()
print("Hello,",name)
#output
#What is your name?      afaq abbas    
#Hello, afaq abbas


#capitalize only make the first letter of output capital 
name = input("What is your name? ").capitalize()
print("Hello,",name)
#output
#What is your name? afaq abbas    
#Hello, Afaq abbas


#title will capitalize the first letter of every sentence in the output
name = input("What is your name? ").title()
print("Hello,",name)
#output
#What is your name? afaq abbas    
#Hello, Afaq Abbas

#combined code
name = input("What is your name? ").strip().title()
print("Hello,",name)
#What is your name?      afaq abbas
#Hello, Afaq Abbas