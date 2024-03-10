# Write a Python program to count the number of even and odd numbers from a series of numbers.
n = int(input("Enter the last number = "))
even =0
odd =0
for i in range(1, n+1):
    if(i%2==0):
        even+=1
    else:
        odd+=1

print("Even number in given range = ", even)
print("ODD number in given range = ", odd)