"""Write a function called showNumbers that takes a parameter called limit. It
should print all the numbers between 0 and limit with a label to identify the
even and odd numbers. For example, if the limit is 3, it should print:
1. 0 EVEN
2. 1 ODD
3. 2 EVEN
4. 3 ODD"""

limit = int(input("Enter the number = "))

def showNumber():
    for i in range(0, limit+1):
        if(i%2==0):
            print(i, " ", "Even")
        else:
            print(i, " ","ODD")
            
showNumber()