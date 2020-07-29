'''
Jesus Manuel Rodriguez Castro
11/13/2019
Assignment 6

A certain college classifies students according to credits earned.
A student with less than 7 credits is a Freshman.
At least 7 credits are required to be a Sophomorem,
16 to be Junior and 26 to be classified as a Senior
Write a program that calculates class standing from
the number of credits earned.

'''


def main():
    credit=int(input("Enter credits: "))
    if credit ==0:
        print("You are not a student of this college!")
    elif credit <=6:
        print("You are a Freshman!")
    elif credit <=15:
        print("You are Sophomore!")
    elif credit <=25:
        print("You are Junior!")
    elif credit == 26:
        print("You are Senior!")
    else:
        print("You are almost a teacher!")
main()
        
             

            

        
