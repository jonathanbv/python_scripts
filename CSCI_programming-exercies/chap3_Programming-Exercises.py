#an interactive program that combines the programming exercises for
#chapter 3 in Programming Logic & Design
#may upgrade to a gui version using tkinter once we get the logic down...

##function definitions
#present menu to user and accept input
import traceback
running = True

def presMenu():
    print("Welcome to the Chapter 3 programming exercises")
    print("The following programs are available:")
    print("""
    1. Kilometer Converter
    2. Sales Tax
    3. Insurance Amount Calculator
    4. Automobile Costs
    5. Property Tax
    6. Body Mass Index
    7. Calories from Fat and Carbohydrates
    8. Stadium Seating
    9. Paint Job Estimator
    10. Monthly Sales Tax
    11. Hot Dog Cookout
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
            kmConverter()
        elif progNumber == 2:
            salesTax()
        elif progNumber == 3:
            insuranceAmount()
        elif progNumber == 4:
            autoCosts()
        elif progNumber == 5:
            propTax()
        elif progNumber == 6:
            bodyMassIndex()
        elif progNumber == 7:
            calFromFatAndCarb()
        elif progNumber == 8:
            stadiumSeating()
        elif progNumber == 9:
            paintJob()
        elif progNumber == 10:
            monthlySalesTax()
        elif progNumber == 11:
            hotDog()
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
def kmConverter():
    try:
        miles = float(input("Enter distance in miles: "))
        kms = miles * 0.6214
        print("{mls: .4g} miles is {kilos: .4g} kilometers.".format(mls=miles, kilos=kms))
    except:
        print("Invalid input.")
def salesTax():
    def countyTax(num):
        rate = 0.01
        tax = num * rate
        return tax, rate
    def stateTax(num):
        rate = 0.02
        tax = num * rate
        return tax, rate
#right-aligning monetary amounts makes the periods all line up :)
    itemCost = float(input("Enter the cost of the item:"))
    print()
    print(f"{'County Tax':<20}${itemCost:10.2f} @ {countyTax(itemCost)[1]:<15.0%}${countyTax(itemCost)[0]:>10.2f}")
    print(f"{'State Tax':<20}${itemCost:10.2f} @ {stateTax(itemCost)[1]:<15.0%}${stateTax(itemCost)[0]:>10.2f}")
    print(f"{'All Tax':<49}${stateTax(itemCost)[0] + countyTax(itemCost)[0]:>10.2f}")
    print(f"{'Total':<49}${stateTax(itemCost)[0] + countyTax(itemCost)[0] + itemCost:>10.2f}")

def insuranceAmount():
    def sureCalc(num):
        return num * .80
    try:
        value = float(input("Hey kid, what's the replacement cost of your building? $"))
        print("We suggest you purchase ${:.2f} of insurance on the property. Sign here.".format(sureCalc(value)))
    except:
        print("invalid input")

def autoCosts():
    #another opportunity to experiment with string formatting
    def monthsum(*args):
        sum = 0
        for arg in args:
            sum += arg
        return sum
    iArgs = []
    costs = {"loan" : 0,
             "insurance": 0,
             "gas": 0,
             "oil": 0,
             "tires":0,
             "maintenance": 0}

    for key in costs:
        costs[key] = float(input("Enter monthly cost of {}: ".format(key)))
        iArgs.append(costs[key])

    print(f"{'Monthly Vehicle Cost':-^50}")

    for k, v in costs.items():
        print("{:<40}${:>10.2f}".format(k,v))
    print(f"{'Total Monthly Cost':<40}${monthsum(*iArgs):>10.2f}")

def propTax():
    def assessValue(num):
        ass = num * 0.60
        tax = (ass/100) * 0.64
        return ass, tax
    value = float(input("Enter the property value: $"))
    print()
    print("{assP:20}${:>10.2f}\n{taxP:20}${:>10.2f}".format(assP="Assessed Value:",taxP="Tax:",*assessValue(value)))

def bodyMassIndex():
    weight = float(input("\nEnter your weight in kg:"))
    height = float(input("Enter your height in meters:"))
    bmi = weight * height
    print(f"\n{'Weight:':<10}{weight:>10.2f}kg\n{'Height:':<10}{height:>10.2f}m\n{'BMI:':<10}{bmi:>10.2f}")

def calFromFatAndCarb():
    def calsFrom(fatG, carbG):
        fromFat = fatG * 9
        fromCarb = carbG * 4
        return fromFat, fromCarb
    fatIn = float(input("Enter grams of Fat:"))
    carbIn = float(input("Enter grams of Carb:"))
    output = calsFrom(fatIn,carbIn)
    print("Cals from fat {:>10}\nCals from carbs {:>10}".format(*output))
    #i'm realizing that dictionaries are potentially clutch when it comes to pretty printing
def stadiumSeating():
    seats = [
    ["Class A",15,None],
    ["Class B",12,None],
    ["Class C",9, None],
    ]

    total = 0
    attends = 0

    for list in seats:
        list[2] = int(input("Enter number of {} tickets sold: ".format(list[0])))
        attends =+ list[2]
        total += list[1] * list[2]
    print()
    print(f"{'Ticket Sales':*^51}")
    print(f"{'Class':<16}{'Cost':>10}{'Quantity':>15}")
    print('-'*51)
    for list in seats:
        print("{:<15}${:>10.2f}{:>15}".format(*list))
    print('-'*51)
    print(f"{'Total':<15}${total:>10.2f}{attends:>15}")

def paintJob():
    def paintCalc(sqft,perBucket):
        gal = sqft / 115
        hrs = gal * 8
        labCost = hrs * 20
        matCost = gal * perBucket
        return gal, hrs, (labCost + matCost)
    paintPut = float(input("Enter square feet to be painted: "))
    paintCost = float(input("Enter cost per bucket of paint: "))
    print("""Your project will use:
            {:.2f} gallons of paint
            {:.2f} hours of labor
            ${galC:.2f} per gallon of paint
            $20 per hour of labor
            Total Cost: ${:.2f}""".format(galC=paintCost,*paintCalc(paintPut,paintCost)))
def monthlySalesTax():
    STATE_TAX = 0.04
    COUNTY_TAX = 0.02
    monthSales = float(input("Enter total monthly sales: $"))
    print()
    print(f"{'COUNTY TAX':<15}${monthSales:12.2f} @ {COUNTY_TAX:<15.0%}${COUNTY_TAX * monthSales:>10.2f}")
    print(f"{'STATE TAX':<15}${monthSales:12.2f} @ {STATE_TAX:<15.0%}${STATE_TAX * monthSales:>10.2f}")
    print(f"{'ALL TAX':<46}${COUNTY_TAX * monthSales + STATE_TAX * monthSales:>10.2f}")

def hotDog():
    peeps = int(input("Enter number of attendees: "))
    dogPerPeep = int(input("Enter number of dogs per person:"))

    dogTotal = peeps * dogPerPeep

    dogPkg = dogTotal // 10 + (dogTotal % 10 > 0)
    bunPkg = dogTotal // 8 + (dogTotal % 8 > 0)

    dogRemain = (dogPkg * 10) - dogTotal
    bunRemain = (bunPkg * 8) - dogTotal

    print("{} dogs and {} buns will be leftover.".format(dogRemain,bunRemain))
    print("Sounds like a great party.")

##run the program
executeSelection()
