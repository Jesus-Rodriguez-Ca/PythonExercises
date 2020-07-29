# Assignment 1 "Convert"
# A program that prints an introduction that tells the user what the program does. 
# Jesus Manuel Rodriguez Castro
# 09/12/2019

# A program to convert Celsius temps to Fahrenheit

def main():
    print(" This program will convert Celsius temperatures to Fahrenheit")
    celsius = eval(input("What is the Celsius temperature you would like to know? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degreess Fahrenheit.")

main()
