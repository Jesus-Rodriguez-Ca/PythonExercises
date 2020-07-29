'''
Jesus Manuel Rodriguez Castro
11/18/2019
Peer Assignment 8


This class represents a playing card
it will contain a cumber and suit
'''

class Card():
    def __init__(self, rank, suit):
        self.rank=rank
        self.suit=suit
        self.value=0

    def getSuit(self):
        return self.suit

    def getRank(self):
        return self.rank

    def setValue(self):
        if self.rank > 10:
            self.value=10
        else:
            self.value= self.rank
        return self.value

    def getsuit(self):
        self.s=""
        if self.suit=="d":
            self.s="Diamonds"
        elif self.suit=="h":
            self.s="Hearts"
        elif self.suit=="c":
            self.s="Clubs"
        else:
            self.s="Spades"
        return self.s

    def __str__(self):
        if self.rank> 1 and self.rank <11:
            self.name=str(self.rank) + "of" + self.getSuit()
        if self.rank==1:
            self.name = "The Ace of" + self.getsuit()
        if self.rank ==11:
            self.name="The jack of " + self.getsuit
        if self.rank==12:
            self.name="The Queen of" + self.getsuit()
        if self.rank==13:
            self.name="The king of" + self.getsuit()
        return self.name
    

