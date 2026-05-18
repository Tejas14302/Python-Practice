a=int(input("Enter The Value Of A:"))
b=int(input("Enter The Value Of B:"))
c=int(input("Enter The Value Of C:"))
d=int(input("Enter The Value Of D:"))
print()
if a==b and b==c and c==d:
    print("All Have Same Value.")
else:
    if a>b:
        if a>c:
            if a>d:
                print("A Is Maximum.")
            else:
                print("D is Maximum.")
        else:
            if c>d:
                print("C is Maximum.")
            else:
                print("D Is Maximum.")
    else:
        if b>c:
            if b>d:
                print("B Is Maximum.")
            else:
                print("D is Maximum.")
        else:
            if c>d:
                print("C Is Maximum.")
            else:
                print("D is Maximum.")
'''
    output:
    1.
    Enter The Value Of A:12
    Enter The Value Of B:13
    Enter The Value Of C:14
    Enter The Value Of D:15

    D is Maximum.

    2.
    Enter The Value Of A:12
    Enter The Value Of B:13
    Enter The Value Of C:44
    Enter The Value Of D:15

    C Is Maximum.

    3.
    Enter The Value Of A:12
    Enter The Value Of B:33
    Enter The Value Of C:14
    Enter The Value Of D:15

    B Is Maximum.

    4.
    Enter The Value Of A:22
    Enter The Value Of B:12
    Enter The Value Of C:13
    Enter The Value Of D:14

    A Is Maximum.

    5.
    Enter The Value Of A:12
    Enter The Value Of B:12
    Enter The Value Of C:12
    Enter The Value Of D:12

    All Have Same Value.
'''                    