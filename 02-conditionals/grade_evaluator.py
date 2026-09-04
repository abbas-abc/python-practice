grades = input("Enter your grade: ")

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



