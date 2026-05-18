a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
c=int(input("Enter third Number:"))
print()
if a==b and b==c:
    print("All Are Same Numbers.")
else:
    if a<b:
        if a<c:
            print("First Number Is Minimum.")
        else:
            print("Third Number Is Minimum.")
    else:
        if b<c:
            print("Second Number is Minimum.")
        else:
            print("Third Number is Minimum.")
'''
    output:
    1.
    Enter First Number:12
    Enter Second Number:33
    Enter third Number:44

    First Number Is Minimum.

    2.
    Enter First Number:22
    Enter Second Number:12
    Enter third Number:13

    Second Number is Minimum.

    3.
    Enter First Number:12
    Enter Second Number:13
    Enter third Number:4

    Third Number Is Minimum.

    4.
    Enter First Number:12
    Enter Second Number:12
    Enter third Number:12

    All Are Same Numbers.
'''