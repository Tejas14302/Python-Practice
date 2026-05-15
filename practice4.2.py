a=int(input("Enter The Value Of A:"))
b=int(input("Enter The Value Of B:"))
c=int(input("Enter The Value Of C:"))
if a>b and a>c:
    print("A Is Largest Number.")
elif b>a and b>c:
    print("B Is Largest Number.")
else:
    print("C Is Largest Number.")
'''
    output:
    1 => Enter The Value Of A:12
         Enter The Value Of B:22
         Enter The Value Of C:33
         C Is Largest Number.

    2 => Enter The Value Of A:55
         Enter The Value Of B:44
         Enter The Value Of C:33
         A Is Largest Number.

    3 => Enter The Value Of A:12
         Enter The Value Of B:55
         Enter The Value Of C:34
         B Is Largest Number.
                  
'''