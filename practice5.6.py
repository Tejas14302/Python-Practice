print("Press 1 For English!")
print("Press 2 For Hindi!")
print("Press 3 For Gujarati!",end="\n\n")
choice=int(input("Your Choice:"))
print()
match choice:
    case 1:
        print("Press 1 For Grammer!")
        print("Press 2 For Speaking!")
        print("Press 3 For Writing!")
        print()
        choice1=int(input("Your Choice:"))
        print()
        match choice1:
            case 1:
                print("You Selected English Grammer!")
            case 2:
                print("You Selected English Speaking!")
            case 3:
                print("You Selected English Writing!")
            case _:
                print("invalid Choice!!!")
    case 2:
        print("Press 1 For Grammer!")
        print("Press 2 For Speaking!")
        print("Press 3 For Writing!")
        print()
        choice2=int(input("Your Choice:"))
        print()
        match choice2:
            case 1:
                print("You Selected Hindi Grammer!")
            case 2:
                print("You Selected Hindi Speaking!")
            case 3:
                print("You Selected Hindi Writing!")
            case _:
                print("invalid Choice!!!")
    case 3:
        print("Press 1 For Grammer!")
        print("Press 2 For Speaking!")
        print("Press 3 For Writing!")
        print()
        choice3=int(input("Your Choice:"))
        print()
        match choice3:
            case 1:
                print("You Selected Gujarati Grammer!")
            case 2:
                print("You Selected Gujarati Speaking!")
            case 3:
                print("You Selected Gujarati Writing!")
            case _:
                print("invalid Choice!!!")
    case _:
        print("Invalid Choice!")
'''
    output:
    Press 1 For English!
    Press 2 For Hindi!
    Press 3 For Gujarati!

    Your Choice:1

    Press 1 For Grammer!
    Press 2 For Speaking!
    Press 3 For Writing!
    Your Choice:1

    You Selected English Grammer!
'''