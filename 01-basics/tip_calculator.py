#tip calculator 

Total_bill = float(input("Enter total bill amount = " ))     #used float becuase it can contain decimal
peoples = int(input("Enter total number of peoples = "))     #int is used becuase the number of people cannot be in decimal
tip_percentage = int(input("enter tip percentage = "))
tip_amount= Total_bill*tip_percentage/100           

print("Each person owns = ", Total_bill/peoples)

Total_with_tip = Total_bill+tip_amount

print("Total amount with tip = ", Total_with_tip)

person_with_tip_own = Total_with_tip/peoples

print("Each person with tip owns = ", person_with_tip_own)
