# Assignment 1
# A program that prints an introduction that tells the user what the program does. 
#Jesus Manuel Rodriguez Castro
#09/12/2019

# A program to convert Celsius temps to Fahrenheit

def main():
    celsius = eval(input("What is the Celsius temperature?"))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degreess Fahrenheit.")

main()