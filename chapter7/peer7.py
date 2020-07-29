'''
This program creates a simple guessing game.
The program creates a random number between 1 and 1000
and the user has 10 chancges to guess the number.
The program responds each guess by telling
the player if their guess is too high, too low, or correct.
Each try statrs with 10 points. Each wrong asnwer
subtracts a point. The players score is however many points
they have when they guess the right answer or 0 if they don't.
At the end of each game the player is akes whether ornot they want to p lay again.
If yes, the game restarts , if not the player is given an average
if their scores and the game quits.
programming steps fro game:

1. Get a ramdon numer
2. Loop for 10 times:
    a. Get the user's quess
    b. Determine it is too high, too low, or correct.
    c. Adjust player score.
3. Display player score.
4. Add score to list if scores.
5. Ask player if they want to play again:
    a. If yes start new game.
    b.If no show average score and quit.

Jesus Manuel Rodriguez Castro.
11/18/2018
Peer Assignement 7
'''

from random import randrange

#Introduccion
def intro():
    print("This program is a simple guessing game.")
    print("The program will generate a random number.")
    print("Between 1 and 1000. You get 10 guesses.")
    print("The game will tell you if the guess is to high")
    print("too low, or correct. Each time you play is worth")
    print("10 points. Each wrong guess subtracts a point.")

def getRandom():
    number= randrange(1, 1001)
    return number
def getUserGuess():
    guess= int(input("Enter a guess between 1 and 1000: "))
    return guess
def evaluateGuess(number, guess):
    state = 0
    if guess> number:
        print("Guess is too high.")
    elif guess <number:
        print(" Guess is too low.")
    else:
        print("Congratulations, you got it")
        state = 1
def play():
    number=getRandom()
    score=10
    for i in range (0,11):
        guess= getUserGuess()
        state= evaluateGuess(number, guess)
        if state ==1:
            break
        score=score-1
    return score

def game():
    choice = "y"
    scores=[]
    while choice == "y":
        score=play()
        print("Your score was",score)
        scores.append(score)
        choice=input("Play another game? y to continue: ")
        choice.lower()
    return scores

def getAverageScores(scores):
    total=0
    for item in scores:
        total++item
        average=total/len(scores)
        return average

def printAverage(average):
    print("Your average score was: ", average)

def main():
    intro()
    scores=game()
    avg=getAverageScores(scores)
    printAverage(avg)

main()
    
        
            
        

    
