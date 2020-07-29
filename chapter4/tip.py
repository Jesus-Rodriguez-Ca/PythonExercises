'''
Jesus Manuel Rodriguez Castro
11/11/2019
Assigment 4

Create a program that calculates a tip.
1.Make separate functions to take in the meal amount
2.Get the tip percent
3.Calculate the tip amount
4.Output the result.
** Four functions plus the main that will call the other functions.**
'''

def intro(): #What thi program does.
    print(" This program calculates a tip")

def meal(): # This is to know the inicial amount without tip.
    amount=eval(input("Enter amount to pay without tips: "))
    return amount

def tip():
    tips= .15 # Tips in Seattle area for a good service.
    return tips
def definicion(): #Assigning variables to functions. 
    t=tip()
    a=meal()
    pay= a + (a*t)
    print("Your total to pay is $",float(pay))
    print("You left $",float(a*t) , "on tips")
   

def main():
    intro()
    definicion()

main()
    
    




    
