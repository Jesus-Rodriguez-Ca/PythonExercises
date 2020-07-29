'''
peer assignment 5
steps :
1. Get a sentence from the user.
2. Split the sentence to get an array of the words.
3. Loop through the list of words.
4. Get the length of each word.
5. Total the lengths of all the words.
6. Divide the total lengths by number of words in the list.
Jesus Manuel Rodriguez Castro
10/29/2019
'''

def main():
    print("This program returns the average number of words for a sentence")
    sentence=input("Enter a sentence: ")
    words = sentence.split() #Divide by commas sentence.split('.')
    totalLength=0
    for w in words:
        totalLength += len(w)
    averageLength=totalLength / len(words)
    print("The average length of a word is {0:0.1f}".format(averageLength))

main()
    
          
