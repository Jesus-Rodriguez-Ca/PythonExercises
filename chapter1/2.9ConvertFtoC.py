# This is a program that converts temperatures from Fahrenheit to Celsius.
#Jesus Manuel Rodriguez Castro
#9/13/2019

def main():
    print(" I can convert temperature from Fahrenheit to Celsius for you ")
    fahrenheit = eval(input(" Enter the temperature in Fahrenheits that you would like to convert to Celsius "))
    celsius = (fahrenheit - 32) / 1.8
    print(" The temperature is", celsius, " degrees Celsius ")

main()
