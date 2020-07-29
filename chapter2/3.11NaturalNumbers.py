#Assignment 2 2.11
#Jesus Manuel Rodriguez Castro
#9/26/2019
#Find the sum of the number "n" natural numbers where the value of "n" is provided by the user.

def main():
    print("This program will sum the amount of consecutive numbers that you provide")
    number = eval(input(" Enter the amount of the natural numbers that will be sum: "))
    total = 0
    for number in range(1,number+1):
        total = total + number
    print(total)

main()

    
