a=input("Enter Any String:")
print(a.startswith('Hello')and a.endswith('World'))
b='Data123#science'
print("".join(filter(str.isalpha,b)))
'''
    output:
    1.
    Enter Any String:Hello World 
    True
    Datascience

    2.
    Enter Any String:hello world
    False
    Datascience
'''