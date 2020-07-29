#assignment 3
#Jesus Manuel Rodriguez Castro
#10/17/2019
#A program that makes an acronym from a sentence. 



def main():
    print(" I'll make an acronym from your sentence. ")
    sentence = input(" Enter a sentence and I will make its acronym: ")
    word= sentence.split()
    acronym= ''
    for p in word:
        acronym=acronym + p[0]
    print(acronym.upper())
main()
    
