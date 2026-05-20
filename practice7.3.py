a=input("Enter Any string:")
print(a)
for i in a:
    if i in 'aeiouAEIOU':
        continue
    print(i,end="")
'''
    output:
    Enter Any string:python
    python
    pythn
'''