'''
Jesus Manuel Rodriguez Castro
11/12/2019
Assignment 5

6.11 Write and test function that takes in a list and returns
the square of each number.

Meet this specifications.
1.squareEach(nums) nums is a list of numbers.
2.Modifies the list by squaring each entry.
'''


def squareEach(num1,num2,num3):
    square= num1**2,num2**2,num3**2
    print("The square of those numbers are: ",square)

squareEach(eval(input("num1: ")),eval(input("num2: ")),eval(input("num3: ")))
