# Find the giver number in list
numbers = [1,2,3,4,5,6,7,8,9,10]

num = int(input("Enter the number = "))
index = -1
for i in numbers:
    if(i==num):
        index = i
        break

if(index!=-1):
    print("Element present at = ", index)
else:
    print("Element not Present")
    
