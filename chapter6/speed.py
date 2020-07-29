'''
Jesus Manuel Rodriguez Castro
10/13/2019
Assignment 6

    The speeding ticket fine policy in Podunkville is $50 plus
$5 for each mph over the limit plus a penalty of $200 for any
speed over 90 mph. Write a program that accepts a speed limiy
and a clocked speed and either prints a message indicating the
speed was legal or prints the amount of the fine, if the speed is illegal.

1. Print program action
2. Set variable
3. Use conditions for over speeding
4. Print legal or illegal.

*Considerings*
a) $50.00 for over speeding
b)  $5.00 for each mpg over limit
c) $200.00 if speed over 90 mph.
'''

overspeed = 50
mile = 5
higterspeed = 200
def main():
    print("This program calculate the fine that you have to pay for over speeding. ")
    limit= int(input("Enter the speed limit of the road you were driving at: "))
    speed=int(input("Enter at what speed you were drinving: "))
    if speed >= 90:
        fine = ((speed - limit) * mile + higterspeed + overspeed)
        print("You have to pay: ${0:0.2f}".format(fine))
    elif speed <= limit:
        print("You are respecting the speed limit. Great job!")
    else:
        print("You have to pay: ${0:0.2f}".format((speed - limit) * mile +  overspeed))
                        
main()

    
    
   
    
          
