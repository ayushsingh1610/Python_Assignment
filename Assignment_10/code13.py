# Write a program using variable length arguments to sum up the numbers till values given in function.

def func_input(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum 
print("Sum is = ", func_input(1,2,3,4,5,6,7,8,9,10))
    