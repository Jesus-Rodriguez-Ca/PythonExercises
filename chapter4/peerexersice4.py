#Jesus Manuel Rodriguez Castro
#10/20/2019
#Peer Assigment 4
#steps: 1. Get the number of values to be enter from the user.
#       2. Prompt the user for each numbre
#       3. Total the numbers.
#       4. Print the total

def main():
    print("This program will total values entered by the user. ")
    n=eval(input("How many values do you want to enter? "))
    total=0
    for i in range(n):
        num = eval(input("Enter a number: "))
        total += num # same as total=num + num
    print("Your total is", total)

main()
