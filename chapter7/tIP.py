'''
Jesus Manuel Rodriguez Castro
13/03/2019
Assigment 7 Class

Create a class called Tip that calculates the amount of a tip.
The program should have mutators and Accesors to take
in the amount of the charge, The percent for the tip,
and the tax rate. The program should have methods that return,
the tip amount and the tax amount and the total.
'''


class Tip():
    def __init__(self, subtotal, tip, tax):
        self.subtotal = subtotal
        self.tip = tip
        self.tax = tax
    
    def setSubtotal(self):
        return self.subtotal

    def setTip(self): 
        return self.subtotal * (self.tip / 100)

    def setTax(self):
        return self.subtotal * (self.tax / 100)

    
def main():

    pay = Tip(eval(input("Enter subtotal: ")),eval(input("Enter tip: ")),eval(input("Enter tax: ")))
    
    print("The subtotal is: ", pay.setSubtotal())
    print("You are leaving: ", pay.setTip(), "on tips.")
    print("You are paying: ", pay.setTax(), "on tax")
    print("Your total to pay is: ", pay.setSubtotal() + pay.setTip() + pay.setTax())
    print("Thanks for coming!")
main()
