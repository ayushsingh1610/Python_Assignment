"""Find the output of each expression if x=4
X=x<<2
X=x>>2
X=x>>3
X=x<<3
"""

num = int(input("Enter the number = "))
print("For 1st Expression = ", num<<2)
print("For 2nd Expression = ", num>>2)
print("For 3rd Expression = ", num>>3)
print("For 4th Expression = ", num<<3)