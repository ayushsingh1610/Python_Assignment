# Write a program to read a 4 digit number through the keyboard and calculate the sum of its digits.
num = int(input("Enter the number = "))
sum = 0
while(num>0):
    r = int(num%10)
    sum = sum + r
    num = num/10
    
print("Sum of digits is = ", sum)