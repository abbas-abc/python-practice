grades = input("Enter your grade: ")
#i use here the matching case to evaluate the grades of the students

match grades:
    case "A":
        print("Excellent")

    case "B":
        print("Good job")

    case "C":
        print("Good")

    case "D":
        print("Fail")

    case _:
        print("Invalid Letter")



