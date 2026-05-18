print("Press 1 For Pizza!")
print("Press 2 For Sandwich!")
print("Press 3 For Burgur!",end="\n\n")
choice=int(input("Your Choice:"))
print()
match choice:
    case 1:
        print("Press 1 For Thin Crust Pizza!")
        print("Press 2 For Cheese Burst Pizza!")
        print("Press 3 For Fresh Dough Pizza!",end="\n\n")
        choice1=int(input("Your Choice:"))
        print()
        match choice1:
            case 1:
                print("Your Thin Crust Pizza Will Be Ready soon!")
            case 2:
                print("Your Cheese burst Pizza Will Be Ready soon!")
            case 3:
                print("Your Fresh Dough Pizza Will Be Ready soon!")
            case _:
                print("Invalid Choice!!!")
    case 2:
        print("Press 1 For Grilled Cheese Sandwich!")
        print("Press 2 For Veggie Delight Sandwich!")
        print("Press 3 for Chicken Sandwich!",end="\n\n")
        choice2=int(input("Your Choice:")) 
        print()
        match choice2:
            case 1:
                print("Your Grilled Cheese Sandwich Will Be Ready soon!")               
            case 2:
                print("Your Veggie Delight Sandwich Will Be Ready soon!")
            case 3:
                print("Your Chicken Sandwich Will Be Ready soon!")
            case _:
                print("Invalid Choice!!!")
    case 3:
        print("Press 1 For Classic Veg Burger!")
        print("Press 2 For Cheese Burger!")
        print("Press 3 For Chicken Burger!",end="\n\n")
        choice3=int(input("Your Choice:"))
        print()
        match choice3:
            case 1:
                print("Your Classic Veg Burger Will Be Ready soon!")
            case 2:
                print("Your Cheese Burger Will Be Ready soon!")
            case 3:
                print("Your Chicken Burger Will Be Ready soon!")
            case _:
                print("invalid Choice!!!")
    case _:
        print("Invalid Choice:")
'''
    output:
    Press 1 For Pizza!
    Press 2 For Sandwich!
    Press 3 For Burgur!
    Your Choice:1

    Press 1 For Thin Crust Pizza!
    Press 2 For Cheese Burst Pizza!
    Press 3 For Fresh Dough Pizza!
    Your Choice:2

    Your Cheese burst Pizza Will Be Ready soon!
'''