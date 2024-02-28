# write a program to read the radius of a sphere from the user and calculate the volume of the sphere.
import math
radius = int(input("Enter the radius of sphere = "))

volume = 4/3 * math.pi * (radius**3)

print("The volume of sphere is = ", volume)