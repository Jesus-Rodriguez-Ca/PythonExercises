'''
Assignment #3
Program that counts the amount words that user enteres
Jesus Manuel Rodriguez Castro
10/17/2019
'''
def main():
    print("This program will count the number of word use in the sentence that you enter")
    word=str(input("Enter the sentence that you want me to count: "))
    print(len(word.split()))
    
main()
