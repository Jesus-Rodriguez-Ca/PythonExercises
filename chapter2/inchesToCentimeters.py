#Peer assignment 2
#Jesus Manuel Rodriguez Castro
#9/25/2019
#This program converts centimeters to inches.
CONVERTION_INCHES_TO_CENTIMETERS=2.54
def main():
    print("This program converts centimeters to inches")
    inches = eval(input("Enter the number of inches: "))
    centimeters = inches * CONVERTION_INCHES_TO_CENTIMETERS
    print(inches,"inches equals", centimeters, "centimeters")

main()
    
                  
