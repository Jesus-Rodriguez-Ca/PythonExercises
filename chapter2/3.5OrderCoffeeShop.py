# Assignment 2 Coffee shop order
# Jesus Manuel Rodriguez Castro
# 9/25/2019
# Calculate the cost of shipping an order
# price $10.50 lb, $0.86 ship per pound, $1.50 fixed overhead
def main():
    print("This program wil calculate the price of shipping an order of coffee from Konditorei")
    order = float(input("How many pounds would you like to get: "))
    price = 10.50
    Total_price = order * price + (0.86 * order) + 1.50
    print("The total cost of you ordes is: $", Total_price, "dollars." "\n""Thanks for shopping with us")
    
    

main()


                
