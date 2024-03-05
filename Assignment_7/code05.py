# Consider a college cricket club in which a student can enroll only if he/she is less than 18 and greater than 15 years old.
name = input("Enter the name = ")
age = int(input("Enter the age = "))
if(age>15 and age<18):
    print(name, "can enroll in club.")
else:
    print(name, "can NOT enroll in club.")
