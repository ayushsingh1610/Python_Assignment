# write a program to prompt year and check whether if it is a leap year or not.
year = int(input("Enter the year = "))
if(year%4==0 or year%100!=0 and year%400==0):
    print(year, "is Leap year.")
else:
    print(year, "is NOT a Leap year.")