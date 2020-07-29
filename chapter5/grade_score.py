'''
Jesus Manuel Rodriguez Castro
10/11/2019
Assigment 5

*Create a function to return a grade (based one 5.3)*
  //Use the function grade(score) that return the letter grade for a score//
**White a program that accepts an exam score as input and prints out the
corresponding grade. **
'''




def intro():
    print(" This program will give you your final grade:" )
    
def grade(score):
    grade=eval(input(" Enter your score(Between 0-100): "))
    while True:
            if grade > 100:
                print("*You are entering an invalid score.*\n Try again!")
                break
            elif grade>=90:    
                print("Your score is A")
            elif grade>=80:
                print(" Your grade is B")
            elif grade>=70:  
                print("Your grade is C")
            elif grade>=60:
                 print("Your grade is D")
            else:
                print("You got an F")
            return score
      
def main():
    intro()
    grade(0)
    
main()

    
