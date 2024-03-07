# Write a program using returning multiple values to calculate square , cube and square root of a number

import math
num = int(input("Enter the number = "))
def calculate():
    return num*num, num*num*num, math.sqrt(num)

square, cube, square_root = calculate()

print("\nSquare value = ", square)
print("Cube value = ", cube)
print("Square root = ", square_root)