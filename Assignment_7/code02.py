"""Write a Python program to construct the following pattern, using a nested for loop.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

for i in range(1,10):
    if(i<=5):
        for j in range(1,i+1):
            print("*", end = " ")
        
    else:
        for j in range(1, 10-i + 1):
            print("*", end = " ")
        
    print()
        