#an interactive program that combines the programming exercises for
#chapter 4 in Programming Logic & Design

##function definitions
#present menu to user and accept input
import traceback
running = True

def presMenu():
    print("Welcome to the Chapter 4 programming exercises")
    print("The following programs are available:")
    print("""
    1. Roman Numerals
    2. Areas of Rectangles
    3. Mass & Weight
    4. Magic Dates
    5. Color Mixer
    6. Book Club Points
    7. Software Sales
    8. Change for a Dollar Game
    9. Shipping Charges
    10. Body Mass Index II
    11. Time Calculator
    12. Leap Year Detector
    """)
    try:
        usrSelection = int(input("Enter the program number you want to run, or a non-numerical input to quit: "))
    except:
        usrSelection = 0
        print("Exiting program...")
    return usrSelection

#execute named program
def executeSelection():
    global running #reference the global variable running

    while running == True:
        progNumber = presMenu()
        if progNumber == 0:
            print("Bye!")
            break
        elif progNumber == 1:
            romanNumerals()
        elif progNumber == 2:
            areaRectangles()
        elif progNumber == 3:
            massWeight()
        elif progNumber == 4:
            magicDates()
        elif progNumber == 5:
            colorMixer()
        elif progNumber == 6:
            bookClub()
        elif progNumber == 7:
            softwareSales()
        elif progNumber == 8:
            changeDollar()
        elif progNumber == 9:
            shippingCharges()
        elif progNumber == 10:
            bmi_improved()
        elif progNumber == 11:
            timeCalc()
        elif progNumber == 12:
            leapYear()
        else:
            print("Invalid progam selection")
            #error returns to original prompt
            #quit ends program

        usrQuery = input('\nWould you like to run another program? (y/n)')
        if usrQuery == 'y' or usrQuery == 'Y' or usrQuery =='yes' or usrQuery == 'Yes':
            pass
        else:
            running = False
            print("Alright then, goodbye.")


#the challenge for chap 3 is to make them modular...not sure how relevant
#that is since I already have them in modules
def romanNumerals():
    useNum =int(input("Enter a number between 1 and 10:\n"))
    if useNum < 1 or useNum > 10:
        print("Input rejected. Asshole.")
    else:
        if useNum == 1:
            print("I")
        elif useNum == 2:
            print("II")
        elif useNum == 3:
            print("III")           
        elif useNum == 4:
            print("IV")           
        elif useNum == 5:
            print("V")           
        elif useNum == 6:
            print("VI")  
        elif useNum == 7:
            print("VII")
        elif useNum == 8:
            print("VIII")
        elif useNum == 9:
            print("IX")
        elif useNum == 10:
            print("X")   
def areaRectangles():
    wid1 = int(input("Enter the width of rectangle 1: "))
    hgt1 = int(input("Enter the height of rectangle 1: "))
    wid2 = int(input("Enter the width of rectangle 2: "))
    hgt2 = int(input("Enter the height of rectangle 2: "))
    print()

    area1 = wid1 * hgt1
    area2 = wid2 * hgt2

    print("Area 1: {}".format(area1))
    print("Area 2: {}".format(area2))
    print()

    if area1 > area2:
        print("Rectangle 1 has the larger area.")
    elif area2 > area1:
        print("Rectangle 2 has the larger area.")
    else:
        print("The rectangles have equal areas.")
def massWeight():
    mass = float(input("Enter mass of object "))
    if mass > 1000:
        print("Too heavy.")
        return None
    if mass < 1:
        print("Too light.")
        return None

    weight = mass * 9.8
    print("Weight of object is {:.2f} pounds.".format(weight))

def magicDates():
    month = int(input("Enter month (as number): "))
    day   = int(input("Enter day: "))
    year  = int(input("Enter last two digits of year: "))

    if month * day == year:
        print("It's magic, woop!")
    else:
        print("No magic detected.")
    
def colorMixer():
    validColor = ["red","blue","yellow"]
    color1 = input("Enter color 1 (red, blue, or yellow): ")
    color2 = input("Enter color 2 (red, blue, or yellow): ")
    inColor = list()
    if color1 not in validColor or color2 not in validColor: 
        print("invalid input")
        return None
    else:
        inColor.append(color1)
        inColor.append(color2)

    if validColor[0] in inColor and validColor[1] in inColor:
        print("Resulting color is purple.")
    elif validColor[0] in inColor and validColor[2] in inColor:
        print("Resulting color is orange.")
    elif validColor[1] in inColor and validColor[2] in inColor:
        print("Resulting color is green.")

def bookClub():
    bookNum = int(input("Enter number of books purchased: "))
    if bookNum <= 0:
        print("Points earned: 0")
    elif bookNum == 1:
        print("Points earned: 5")
    elif bookNum == 2:
        print("Points earned: 15")
    elif bookNum == 3:
        print("Points earned: 30")
    elif bookNum >= 4:
        print("Points earned: 60")

def softwareSales():
    saleQuant = int(input("Enter number of softwares purchased: "))

    if saleQuant >= 100:
        discount = 0.5
    elif saleQuant >= 50:
        discount = 0.4
    elif saleQuant >= 20:
        discount = 0.3
    elif saleQuant >= 10:
        discount = 0.2
    else:
        discount = 0

    subTotal = saleQuant * 99
    savings = subTotal * discount
    total = subTotal - savings

    print("Your total cost is {:.2f}. You saved {:.2f} ({:.0%})".format(total,savings,discount))

def changeDollar():
    pennies = int(input("Enter number of pennies: "))
    nickels = int(input("Enter number of nickels: "))
    dimes = int(input("Enter number of dimes: "))
    quarters = int(input("Enter number of quarters: "))

    value = pennies * 1 + nickels * 5 + dimes * 10 + quarters * 25
    dollars = value // 100
    cents = value % 100

    print(f"You have ${dollars}.{cents:02d}")
    if dollars == 1 and cents == 0:
        print("You WON the dollar game.")
    else:
        print("You LOST the dollar game.")
def shippingCharges():
    weight = float(input("Enter weight of package in lbs: "))
    if weight > 10:
        rate = 3.8
    elif weight > 6:
        rate = 3.7
    elif weight > 2:
        rate = 2.2
    else:
        rate = 1.1

    cost = weight * rate
    print("Your shipping cost is: {:.2f}".format(cost))

def bmi_improved():
    weight = float(input("enter weight in kilograms: "))
    height = float(input("enter height in meters: "))

    bmi = weight / height**2
    print("Your bmi is {}".format(bmi))
    print("calculating weight fatassery...")
    
    if bmi < 18.5:
        print("Underweight. Go eat cheeseburg.")
    elif bmi > 25:
        print("Overweight. Stop eat cheeseburg.")
    else:
        print("Your weight is okay.")
def timeCalc():
    seconds = float(input("Enter number of seconds: "))
    if seconds >= 86400:
        days = seconds / 86400
        print(f"There are {days:.2f} days in {seconds} seconds.")
    elif seconds >= 3600:
        hours = seconds / 3600 
        print(f"There are {hours:.2f} hours in {seconds} seconds.")
    elif seconds >= 60:
        minutes = seconds / 60
        print(f"There are {minutes:.2f} minutes in {seconds} seconds.")
    else:
        print(f"You entered {seconds} seconds.")

def leapYear():
    years = int(input("Enter the year of interest: "))
    if (years % 100 == 0 and years % 400 == 0) or (years % 4 == 0):
        print("It's a leap year! Woopy!")
    else:
        print("It's not a leap year...")



##run the program
executeSelection()
