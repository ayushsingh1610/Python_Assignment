# Print the Even numbers in list
numbers = [1,2,3,5,34,67,34,3,5,78]

print("Evens numbers are = ", end= "")
for i in numbers:
    if(i%2==0):
        print(i, end = "")