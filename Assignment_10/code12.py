# Write a program using returning multiple values to calculate area and perimeter of a rectangle.

length = int(input("Enter the length = "))
breadth = int(input("Enter the breadth = "))

def calculate():
    return length*breadth, 2 * (length + breadth)

area, perimeter = calculate()

print("\nArea of Rectangle = ", area)
print("Perimeter of Rectangle = ", perimeter)
