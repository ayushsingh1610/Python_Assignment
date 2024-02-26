# Write a program to compute distance between two points taking input from the user (Pythagorean Theorem).
import math

x1 = float(input("Enter the x coordinate of 1st point = "))
y1 = float(input("Enter the y coordinate of 1st point = "))
x2 = float(input("Enter the x coordinate of 2nd point = "))
y2 = float(input("Enter the y coordinate of 2nd point = "))

distance =float(math.sqrt((x2-x1)**2 + (y2-y1)**2))

print("The Distance is = ", distance)