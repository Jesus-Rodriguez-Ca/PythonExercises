#Assigment 2
#Jesus Manuel Rodriguez Castro
#10/10/2019
#3.11 sim of cube of n numbers

def main():
    print("This program will sum consecutive cube numbres")
    n=int(input("Enter amount of numbers to sum: "))
    number=1
    for num in range(1,n, +1):
        number = (number + num)**2
    print(number)

main()
    
