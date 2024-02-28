# Write a program to calculate the distance between 2 points. The formula is:     d=√((x2-x1)²+(y2-y1)²)
import math

x1 = int(input("Enter the value of x1 = "))
y1 = int(input("Enter the value of y1 = "))
x2 = int(input("Enter the value of x2 = "))
y2 = int(input("Enter the value of y2 = "))

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print("The distance of two point is = ", distance)