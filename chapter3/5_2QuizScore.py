'''
Assignment 3
5.2 Quiz scores
A program that alows the user to enter his/her grades in numbers and output its value in letters
Jesus Manuel Rodriguez Castro
10/17/2019
'''

def main():
    print(" This program will give you your final scores:" )
    grade=eval(input(" Enter your grade(Between 0-5): "))
    
    if grade > 5:
        print("Enter a number between 0 and 5")
    elif grade==5:    
        print("Your score is A")
    elif grade==4:
        print(" Your grade is B")
    elif grade==3:
        
        print("Your grade is C")
    elif grade==2:
         print("Your grade is D")
    else:
        print("You got an F")

main()
    
