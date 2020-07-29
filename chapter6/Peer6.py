'''
Jesus Manuel Rodriguez Castro
11/12/2019
Peer Assigment 6

Calculate weekly wage with functions
1. Get hours work
2. Get houtly wage
3. Calculate regular pay
4. Calculate overtime pay
5. Calculate weekly pay
6. Print results
'''
REGHOURS=40
def getHours():
    hours=int(input("Enter the hours worked for the week: "))
    return hours

def getWage():
    wage=float(input("Enter the hourly wage: "))
    return wage


def calculateRegularPay(hrs, wage):
    regPay=0
    if hrs > REGHOURS:
        regPay=REGHOURS * wage
    else:
        regPay=hrs * wage
    return regPay

def calculateOvertime(hrs, wage):
    otPay=0
    if hrs>REGHOURS:
        otPay=wage * (hrs-REGHOURS) * 1.5
        
    return otPay

def calculateWeeklyWage():
    h = getHours()
    w = getWage()
    reg = calculateRegularPay(h,w)
    ot= calculateOvertime(h, w)
    total= reg + ot
    printWages(reg, ot, total)

def printWages(reg, ot, total):
    print("Your regular pay is ${0:0.2f}".format(reg))
    print("Your over time pay is ${0:0.2f}".format(ot))
    print("your total pay is ${0:0.2f}".format(total))

def main():
    calculateWeeklyWage()

main()


    
