a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=int(input("Enter Third Number:"))
print()
if a==b and b==c:
    print("All Are Same Numbers.")
else:
    if a>b:
        if a>c:
            print("First Number Is Maximum.")
        else:
            print("Third Number Is Maximun.")
    else:
        if b>c:
            print("Second Number Is Maximum.")
        else:
            print("Third Number Is Maximum.")
'''
    output:
    1.
    Enter First Number:12
    Enter Second Number:23
    Enter Third Number:44

    Third Number Is Maximum.

    2.
    Enter First Number:12
    Enter Second Number:2
    Enter Third Number:4

    First Number Is Maximum.

    3.
    Enter First Number:13
    Enter Second Number:44
    Enter Third Number:55

    Third Number Is Maximum.

    4.
    Enter First Number:12
    Enter Second Number:12
    Enter Third Number:12

    All Are Same Numbers.
'''