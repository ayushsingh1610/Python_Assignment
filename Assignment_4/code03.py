# Read two integers and perform all arithmetic operations on those two numbers.

num1 = int(input("Enter the 1st numbeer = "))
num2 = int(input("Enter the 2nd number = "))

addition = int(num1 + num2)
mutiplication = int(num1 * num2)
if(num2>num1):
    subtraction = int(num2 - num1)
    division = float(num2/num1)
    
else:
    subtraction = int(num1 - num2)
    division = float(num1/num2)


print("The addition of two numbers is = ", addition)
print("The subtraction of two numbers is = ", subtraction)
print("The mutiplication of two numbers is = ", mutiplication)
print("The division of two numbers is = ", division)
