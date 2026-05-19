sy=int(input("Enter Starting Year:"))
fy=int(input("Enter Finishing Year:"))
while sy<=fy:
    if sy%4==0:
        print("All The Leap Years Between Starting And Finishing Year Are:",sy)
    sy+=1 
'''
    output:
    Enter Starting Year:2016
    Enter Finishing Year:2025
    All The Leap Years Between Starting And Finishing Year Are: 2016
    All The Leap Years Between Starting And Finishing Year Are: 2020
    All The Leap Years Between Starting And Finishing Year Are: 2024
'''       