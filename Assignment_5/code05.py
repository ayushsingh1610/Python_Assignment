# Write a program to read an integer as string. Convert the string into integer and display the type of value before and after converting to int.

num = input("Enter the number = ")
print(num , type(num))
num = int(num)
print(num , type(num))