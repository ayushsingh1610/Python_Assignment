# Write a Python function to find the Max of three numbers. 

num1 = int(input("Enter the 1st number = "))
num2 = int(input("Enter the 2nd number = "))
num3 = int(input("Enter the 3rd number = "))

def max():
    if(num1>num2 and num1>num3):
        return num1
    elif(num2>num1 and num2>num3):
        return num2
    else:
        return num3
    
print("Maximum of three is = ", max())