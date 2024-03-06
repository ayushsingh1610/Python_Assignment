"""Write a function for checking the speed of drivers. This function should have
one parameter: speed.
I. If speed is less than 70, it should print “Ok”.
II. Otherwise, for every 5km above the speed limit (70), it should give
the driver one demerit point and print the total number of demerit
points. For example, if the speed is 80, it should print: “Points: 2”.
III. If the driver gets more than 12 points, the function should print:
“License suspended”
    """
    
speed = int(input("Enter the speed = "))

def check_speed():
    if(speed<=70):
        print("OK")
    else:
        point = int((speed - 70)/5)
        if(point > 12):
            print("Licence Suspended.")
        else:
            print("Points : ", point)
        
check_speed()