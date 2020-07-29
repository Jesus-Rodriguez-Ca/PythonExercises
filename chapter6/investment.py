'''
Jesus Manuel Rodriguez Castro
11/13/2019
Assignment 6

Write a program that uses a while loop to detirmen how long it takes
for an investment to double at a given interest rate.
The input will be an annualized interest rate, and the output is the
number of years it takes an investment to doble. Note: The amount of
the initial investment does not matter; you can use $1.

1. Print what to do.
2. Use while loop

**Notes**
Investment formula.
A = P (1 + r/n) (nt)
'''

def initial(p,r,t):
    a = p * (1 + r) ** t
    return a
def main():
    print("This program will tells how long your investment will doubled.")
    prin = eval ( input ( "Enter how much you want to invest: ") )
    interest = eval ( input ( " Enter annually interest: ") )
    while interest > 1:
        interest = interest / 100
        continue
    time = 0
    total = 0
    while total < 2 * prin:
        total = initial(prin,interest,time)
        time= time + 1

    print("If you invest",prin,"dollars with an interest of",interest,"annually it'll take",time,"years to doubled.")

main()
        

    
    
    
    
