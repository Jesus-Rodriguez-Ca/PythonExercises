# Assignment 1 " Average"
# This program will find the average of three exam scores.
# Jesus Manuel Rodriguez Castro
# 9/23/2019

def main():
    print(" This program will show you the average of the three exam scores. ")

    score1 = eval(input("Enter the first score  "))
    score2 = eval(input("Enter the second score "))
    score3 = eval(input("Enter the third score  "))
    average = (score1 + score2 + score3) / 3

    print(" The average of the scores is:", average)

main()
