# This is peer assigment 1
# Modidy the chaos program to allow the user to set the number of values to print.
# Jesus Manuel Rodriguez Castro
#9/23/19

def main():
    print ("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    count = eval(input(" Enter the number of values you want to output:  "))
    for i in range(count):
        x = 3.9 * x * (1 - x)
        print(x)


main() 
    
