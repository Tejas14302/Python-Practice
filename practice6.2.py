n=int(input("Enter Any Number:"))
m=1
sum=0
while m<=n:
    if m%2!=0:
        sum=sum+m
    m+=1
    
print("Sum Of The Odd Numbers Is:",sum)
'''
    output:
    Enter Any Number:10
    Sum Of The Odd Numbers Is: 25
'''