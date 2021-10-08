#an interactive program that combines the programming exercises for
#chapter 2 in Programming Logic & Design

##function definitions
#present menu to user and accept input
import traceback
running = True

def presMenu():
    print("Welcome to the Chapter 1 programming exercises")
    print("The following programs are available:")
    print("""
    1. Personal Information
    2. Sales Prediction
    3. Land Calculation
    4. Total Purchase
    5. Distance Traveled
    6. Sales Tax
    7. Miles-per-Gallon
    8. Tip, Tax, Total
    9. Weight Loss
    10. Amount Paid Over Time
    11. Leftover Pizza
    12. Celsius to Farenheit
    13. Stock Transactions
    """)
    try:
        usrSelection = int(input("Enter the program number you want to run, or a non-numerical input to quit: "))
    except:
        usrSelection = 0
        print("Exiting program...")
    return usrSelection

#execute named program
#while loop could result in cleaner looping
def executeSelection():
    global running #reference the global variable running

    while running == True:
        progNumber = presMenu()
        if progNumber == 0:
            print("Bye!")
            break
        elif progNumber == 1:
            personal_info()
        elif progNumber == 2:
            sales_predict()
        elif progNumber == 3:
            land_calc()
        elif progNumber == 4:
            total_purchase()
        elif progNumber == 5:
            distance_travelled()
        elif progNumber == 6:
            sales_tax()
        elif progNumber == 7:
            mpg()
        elif progNumber == 8:
            tip_tax()
        elif progNumber == 9:
            weight_loss()
        elif progNumber == 10:
            amount_paid()
        elif progNumber == 11:
            lefover_za()
        elif progNumber == 12:
            celsiusToF()
        elif progNumber == 13:
            stonks()
        #elif progNumber == 14:
        #    cookie()
        #elif progNumber == 15:
        #    maleFemale()
        #elif progNumber == 16:
        #    ingredients()
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

#1 personal information
def personal_info():
    print("Program 1: Personal Information")
    usrName = input("Enter your name:")
    usrAddress = input("Enter your address:")
    usrPhone = input("enter your phone number:")
    usrMajor = input("enter your college major:")

    print("We collected the following information:")
    print("Name: ", usrName)
    print("Address: ", usrAddress)
    print("Phone Number: ", usrPhone)
    print("usrMajor: ", usrMajor)

    #User inputs personal information and it is displayed by program
    #include Name, address, city, state, zip, telephone # and college major

#2 sales prediction
def sales_predict():
    print("Program 2: Sales Prediction")
    sales = int(input("Enter the sales in $:"))
    profit = sales * .23
    print("Total profit during the period was $", profit)
    #given 23% profit margin, program displays projected profits when given sale

#3 land calculation
#how to clean up numeric output?
def land_calc():
    print("Program three: Land Calculation")
    print("one acre is 43,560 square feet")
    sqFeet = int(input("How many square feet do you have?"))
    acreage = sqFeet / 43560
    print("You have ",acreage, "acres.")
    #program outputs acres when given square feet

#4 Total purchase
def total_purchase():
    print("Program 4: Total Purchase")
    prices = list()
    items = True
    index = 1
    subTotal = 0.0
    tax = 0.0
    total = 0.0

    while items == True:
        curItem = input("Enter the price of item number " + str(index) + "(Enter any non-numerical value to finish): ")
        try:
            prices.append(float(curItem))
            index += 1
        except Exception:
            traceback.print_exc()
            print("You entered a non-numerical value. Calculating total price...")
            items = False

    for price in prices:
        subTotal += price
        tax += price* 0.06
    total = subTotal + tax

    print("Number of items: ", len(prices))
    print("Subtotal: $", subTotal)
    print("Tax: $", tax)
    print("Total Price: $", total)

#5 Distance Travelled
def distance_travelled():
    print("Program 5: Distance Traveled")
    speed = int(input("Enter vehicle speed in mph: "))
    time = int(input("Enter number of hours traveled: "))
    distance = speed * time
    print("Vehicle traveling at ", speed, "mph will travel ",distance, " miles in ",time," hours.")

#6 Sales tax
def sales_tax():
    print("Program 6: Sales Tax")
    price = float(input("Enter price of item: "))
    state_tx = price * 0.04
    county_tx = price * 0.02
    total_tx = state_tx + county_tx
    total_cost = price + total_tx
    print("Item Purchase Price: $", price)
    print("State sales tax: $", state_tx)
    print("County sales tax: $", county_tx)
    print("Total tax: $", total_tx)
    print("Total cost: $", total_cost)

#7 Miles-per-Gallon
def mpg():
    print("Program 7: Miles per Gallon")
    miles = int(input("Enter miles driven: "))
    gallons = int(input("Enter number of gallons consumed: "))
    mpg = miles / gallons
    print("MPG of vehicle is ", mpg)

#8 Tip, tax, total
def tip_tax():
    print("Program 8: Tip, Tax, Total")
    food = float(input("Enter cost of food: $"))
    tip = food * .15
    tax = food * .07
    total = food + tip + tax
    print("Meal cost: $",food)
    print("Tip: $", tip)
    print("Tax: $", tax)
    print("Total: $", total)

#9 Weight Loss
def weight_loss():
    print("Program 9: Weight loss")
    start_weight = int(input("Enter your starting weight: "))
    diet_months = int(input("How many months do you plan to diet?: "))
    weightList = list()

    while diet_months > 0:
        weightList.insert(0,start_weight - 4 * diet_months)
        diet_months -= 1

    for weight in weightList:
        print("Month: ",weightList.index(weight)+1, " Expected Weight: ", weight)

    print("Good luck on your weight loss journey.")

#10 Amount Paid over time
def amount_paid():
    print("Program 10: Amount paid over time")
    payment = int(input("Enter your monthly payment: $"))
    months = int(input("Enter number of months you've been making payments: "))
    total = payment * months

    print("So far, you have paid $",total)

#11 leftover pizza
def lefover_za():
    print("Program 11: Pizza Party")
    attend = int(input("Enter number of people attending: "))
    slicesPer = int(input("Enter number slices per pizza: "))
    pizzaQuant = int(input("Enter number of pizzas attending: "))

    sliceTotal = pizzaQuant * slicesPer
    eatTotal = attend * 3
    zaRemain = sliceTotal - eatTotal

    print("With an average consumption rate of three slices per atendee...")
    print(zaRemain, " slices of pizza will remain.")

#12 celsius to farenheit
def celsiusToF():
    print("Program 12: Celsius to Farenheit Converter")
    celsius = float(input("Enter temperature in degrees celsius: "))
    farenheit = celsius * (9/5) + 32
    print("Temperature in farenheit is ",farenheit)

#13 stock transactions
def stonks():
    print("Program 13: Stock Transaction Program")
    buy_price = float(input("\nEnter stock purchase price: $"))
    buy_quant = int(input("Enter number of stocks purchased: "))
    buy_totalStockPrice = buy_price * buy_quant
    buy_comish = buy_totalStockPrice * 0.02
    buy_gTotal = buy_totalStockPrice + buy_comish

    sell_price = float(input("\nEnter stock sale price: $"))
    sell_quant = int(input("Enter number of stocks sold: "))
    sell_totalStockPrice = sell_price * sell_quant
    sell_comish =  sell_totalStockPrice * 0.02
    sell_gTotal = sell_totalStockPrice + sell_comish

    comish_total = sell_comish + buy_comish
    gainOnSale = sell_totalStockPrice - buy_totalStockPrice
    gainLessComish = gainOnSale - comish_total

    print("Transaction summary:")
    print("\nPurchased ", buy_quant, "stocks at $",buy_price," per share.")
    print("Total value of stock purchased: $",buy_totalStockPrice)
    print("Comission paid at purchase: $", buy_comish)
    print("Total paid for purchase: $", buy_gTotal)

    print("\nSold ", sell_quant, "stocks at $",sell_price," per share.")
    print("Total value of stock sold: $",sell_totalStockPrice)
    print("Comission paid at sale: $", sell_comish)
    print("Total paid at sale: $", sell_gTotal)

    print("\nGain on sale: $", sell_gTotal - buy_gTotal)
    print("Total comission paid: $",sell_comish + buy_comish)
    print("Gain less comission: $", gainLessComish)

#14 cookie calories
def cookie():
    print("Program 14: Cookie Calories")
    pass

#15 male and female percents
def maleFemale():
    pass

#16 ingredient adjuster
def ingredients():
    pass

##program Logic
executeSelection()
