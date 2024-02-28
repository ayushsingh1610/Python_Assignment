# Write a program to read the marks of 5 subjects thru the keyboard. Find out the aggregate and percentage of marks obtained by the student. Assume maximum marks that can be obtained by a student in each subject as 100.
english = int(input("Enter the marks of english = "))
hindi = int(input("Enter the marks of hindi = "))
maths = int(input("Enter the marks of maths = "))
science = int(input("Enter the marks of science = "))
computer = int(input("Enter the marks of computer = "))

total_sum = english + hindi + maths + science + computer

percentage = (total_sum * 100)/500

print("Aggregate Percentage = ", percentage, "%")