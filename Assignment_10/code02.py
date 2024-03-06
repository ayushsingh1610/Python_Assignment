"""Write a function called fizz_buzz that takes a number.
I. If the number is divisible by 3, it should return “Fizz”.
II. If it is divisible by 5, it should return “Buzz”.
III. If it is divisible by both 3 and 5, it should return “FizzBuzz”.
IV. Otherwise, it should return the same number."""

num = int(input("Enter the number = "))

def fizz_buzz():
    if(num%3==0):
        return "Fizz"
    elif(num%5==0):
        return "Buzz"
    elif(num%3==0 and num%5==0):
        return "Fizzbuzz"
    else:
        return num
    
print("Answer is = ", fizz_buzz())