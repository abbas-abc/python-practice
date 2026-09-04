#here i use the nesting concept to solve that problem.

question = input("Are you 18 or above? ")

if question == "no":
    print("Ticket price: $6 (child price).")


#i add the student id below else because no more question is needed on below 18 age
else:
    
    student_ID = input("You have the student ID? ")

     
    if question == "yes" and student_ID == "yes":
        print("Ticket price: $8 (student discount).")

    else:
        print("Ticket price: $12 (adult price).")
    
