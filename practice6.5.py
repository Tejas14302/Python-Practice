n=int(input("Enter Any Number:"))
for i in range(1,n+1,1):
    if i%3==0 and i%5==0:
        print("All The Numbers Which Are Divisible by 3 and 5:",i)
'''
    output:
    Enter Any Number:50
    All The Numbers Which Are Divisible by 3 and 5: 15
    All The Numbers Which Are Divisible by 3 and 5: 30
    All The Numbers Which Are Divisible by 3 and 5: 45
'''