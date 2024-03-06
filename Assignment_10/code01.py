# Write a function that returns the maximum of two numbers.

num1 = int(input("Enter the 1st number = "))
num2 = int(input("Enter the 2nd number = "))

def max():
    if(num1 > num2):
        return num1
    else:
        return num2
    
print("Maximum of two number is = ", max())