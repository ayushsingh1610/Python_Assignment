# calculate the sum of 4 digit number both without recursion and with recursion

num = int(input("Enter the number = "))

def recur(num):
    if(num<0):
        return 0
    else:
        num = int(num/10)
        return num%10 + recur(num)

def not_recur(num):
    sum=0
    while(num>0):
        r = num%10
        sum+=r
        num = int(num/10)
    return sum 

print("Answer using Recursion = ", recur(num))
print("Answer without using Recursion = ", not_recur(num))

