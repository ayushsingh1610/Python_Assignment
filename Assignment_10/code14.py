# Write a program using variable length arguments to calculate the average of numbers till the values given in function.

def func_average(*args):
    sum = 0
    for i in args:
        sum+=i
        
    return sum/len(args)

print("Average of all numbers is = ", func_average(2,13,23,24,25,67,45,23))
    
    