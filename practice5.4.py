a=int(input("Enter The Value Of A:"))
b=int(input("Enter The Value Of B:"))
op=input("Take An Operator('+','-','*','/'):")
print()
match op:
    case '+':
        print("The Sum Of A And B Is:",a+b)
    case '-':
        print("The Subtraction Of A And B Is:",a-b)
    case '*':
        print("The Multiplication Of A And B is:",a*b)
    case '/':
        print("The Divison Of A And B Is:",a/b)
    case _:
        print("Invalid Choice!!!")
'''
    output:
    1.
    Enter The Value Of A:12
    Enter The Value Of B:13
    Take An Operator('+','-','*','/'):+

    The Sum Of A And B Is: 25

    2.
    Enter The Value Of A:12
    Enter The Value Of B:13
    Take An Operator('+','-','*','/'):-

    The Subtraction Of A And B Is: -1

    3.
    Enter The Value Of A:12
    Enter The Value Of B:13
    Take An Operator('+','-','*','/'):*

    The Multiplication Of A And B is: 156

    4.
    Enter The Value Of A:4
    Enter The Value Of B:2
    Take An Operator('+','-','*','/'):/

    The Divison Of A And B Is: 2.0

    5.
    Enter The Value Of A:12
    Enter The Value Of B:13
    Take An Operator('+','-','*','/'):#

    Invalid Choice!!!
'''