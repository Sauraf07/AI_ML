x = int(input("Enter a number: "))
match x:
    case 1:
        print("one")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Something else")