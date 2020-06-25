## Author: Michael Kearns
## Last edit: 12/6/19 around 5:00 pm


## All code written here was produced by Michael Kearns
## All code comes form knowledge gained during 
## Summer 2019 Internship at Gilbane Virtual Design and Construction Company 
## and through Professor Carpenter at Wentworth Insitute of Technology



import random
import time



## item class. This is the base class for all menu items
class item:
    itemName = ""
    price = 0
    quantity = 0
    ## Constructors do not get inherited so need a new one for every derived class
    def __init__(self, name, price, quantity):
        self.itemName = name
        self.price = price
        self.quantity = quantity



## Food class, derived from item. This includes the option for a meat filling
class food(item):
    
    meat = ""
    
    def __init__(self, name, price, quantity, meat):
        self.itemName = name
        self.price = price
        self.meat = meat
        self.quantity = quantity
 



 ## Add on class. Derived from food
class addOns(food):
    
    addOnName = ""
 
    def __init__(self, name, price, quantity, AN):
        self.itemName = name
        self.price = price
        self.addOnName = AN  
        self.quantity = quantity  
 

## Drink class. Derived from item
class drink(item):
    size = ""
 
    def __init__(self, name, price, quantity, size):
        self.itemName = name
        self.price = price
        self.size = size
        self.quantity = quantity



## Function for creating a new order list.
## This list contains all the items that a user adds to ther "cart"
## Function returns the list at the end

def createOrder():
    order = []
    order_complete = False
    print("~~~~~~~~~~~~~~~~~~~~~~~\n\tMENU\n~~~~~~~~~~~~~~~~~~~~~~~")
    while(order_complete == False):
        ## Present options for main item, sides, or drinks
        order_choice = input("\n1: Main Items \n2: Sides\n3: Drinks\n4: Complete Order and Continue to payment\nType Choice Here: ")
        ## Present options for main items
        if(order_choice == "1"):
            ##food_choice = input("\tMAIN ITEMS\nItem\t\t\tPrice\n1: Tacos\t\t2: Burritos\t\n3: Tortas\t\t4: Steak and Cheese\n5: Chicken Tenders\n")
            food_choice = input("\nMAIN ITEMS\nItem\t\t\tPrice\n\n1: Taco\t\t\t$2.99\n2: Burrito\t\t$8.99\n3: Torta\t\t$7.99\n4: Steak and Cheese\t$8.99\n5: Chicken Tenders\t$7.99\nType Choice Here: ")
            ## Gather information about Taco order
            if(food_choice == "1"):
                meat_choice = input("\tChoose Meat Filling\n1: Chicken\n2: Steak\nType Choice Here: ")
                if(meat_choice == "1"):
                    quantity = input("Enter quantity: ")
                    order.append(food("Taco", 2.99, quantity, "Chicken"))
                elif(meat_choice == "2"):
                    quantity = input("Enter quantity: ")
                    order.append(food("Taco", 2.99, quantity, "Steak"))
            ## Gather information about Burrito order
            elif(food_choice == "2"):
                meat_choice = input("\tChoose Meat Filling\n1: Chicken\n2: Steak\nType Choice Here: ")
                if(meat_choice == "1"):
                    quantity = input("Enter quantity: ")
                    order.append(food("Burrito", 8.99, quantity, "Chicken"))
                elif(meat_choice == "2"):
                    quantity = input("Enter quantity: ")
                    order.append(food("Burrito", 8.99, quantity, "Steak"))
            ## Gather information about Torta order
            elif(food_choice == "3"):
                quantity = input("Enter quantity: ")
                order.append(item("Torta", 7.99, quantity))
            ## Gather information about Steak and Cheese order
            elif(food_choice == "4"):
                quantity = input("Enter quantity: ")
                order.append(item("Steak and Cheese", 8.99, quantity))
            ## Gather information about Chicken Tender order
            elif(food_choice == "5"):
                quantity = input("Enter quantity: ")
                order.append(item("Chicken Tenders", 8.99, quantity))
            ## User error output
            else:
                print("Invalid input.")

        ## Do similar process for all of the sides 
        elif(order_choice == "2"):
            side_choice = input("\nSIDES\nItem\t\t\t\tPrice\n1: Fries\t\t\t$3.50\n2: Rice and Beans\t\t$4.50\n3: Chips and Salsa\t\t$3.00\nType Choice Here: ")

            if(side_choice == "1"):
                quantity = input("Enter quantity: ")
                order.append(item("Fries", 3.50, quantity))
            elif(side_choice == "2"):
                quantity = input("Enter quantity: ")
                order.append(item("Rice and Beans", 4.50, quantity))
            elif(side_choice == "3"):
                quantity = input("Enter quantity: ")
                order.append(item("Chips and Salsa", 3.00, quantity))
            
        ## Repeat same process for drink order
        elif(order_choice == "3"):
            drink_choice = input("\nDRINKS\nItem\t\t\tPrice\n1: Water\t\t$1.50\n2: Soda\t\t\t$2.00\n3: Homemade Horchata\t$2.50\nType Choice Here: ")
            
            if(drink_choice == "1"):
                size = input("Enter size: ")
                quantity = input("Enter quantity: ")
                order.append(drink("Water", 1.50, quantity, size))
            if(drink_choice == "3"):
                size = input("Enter size: ")
                quantity = input("Enter quantity: ")
                order.append(drink("Soda", 2.0, quantity, size))
            if(drink_choice == "2"):
                size = input("Enter size: ")
                quantity = input("Enter quantity: ")
                order.append(drink("Homemade Horchata", 2.50, quantity, size))
        elif(order_choice == "4"):
            order_complete = True
        
        else:
            print("Invalid input.")

    return order

## Payment Process class. Derived class for all transactions
class paymentProcess:
    customerName = ""
    amount = 0.0

    timeStamp = time.asctime()

    def setCustomerName (self, c):
        self.customerName = c
    def setAmount (self, a):
        self.amount = a

    def __init__(self, custName, amount):
        self.setCustomerName(custName)
        self.setAmountDue(int(amount)*0.07 + int(amount))


## Derived from payment process class. Adds information about card number and confirmation number
class cardPayment(paymentProcess):
    cardNo = 0
    confirmationNo = 0

    def setCardNo (self, c):
        self.cardNo = c


    def __init__(self, custName, amount):
        self.setCustomerName(custName)
        self.setAmount(float(amount))
        self.setCardNo(random.randint(1000,9999))
        self.confirmationNo = random.randint(100,999)

    ## Print receipt function inherited by both credit and debit card payments
    def printReceipt(self):
        print("\n\n\n\tReceipt")
        print("Name: " + self.customerName)
        print("CardNo: XXXXXXXX" + str(self.cardNo))
        print("Confirmation Number: " + str(self.confirmationNo))
        print("Total: $%.2f" %self.amount)
        print("Time : " + str(self.timeStamp))
        print("Signature: ___________\n\n\n\n")




## Debit card class. Derived from cardPayment. So this class is two steps down the inheritance of paymentProcess
## Allows for a pin to stored
class debitCard(cardPayment):
  pin = 0

  def setPin(self, p):
      self.pin = p

  def __init__(self, custName, amount, pin):
      self.setCustomerName(custName)
      self.setAmount(float(amount))
      self.setCardNo(random.randint(1000,9999))
      self.setPin(pin)
      self.confirmationNo = random.randint(100,999)



## Credit Card class. Derived from cardPayment, similar to debit card

class creditCard(cardPayment):
  zipCode = "0"

  def setZip(self, z):
      self.zipCode = z

  def __init__(self, custName, amount, zipCode):
      self.setCustomerName(custName)
      self.setAmount(float(amount))
      self.setCardNo(random.randint(1000,9999))
      self.setZip(zipCode)
      self.confirmationNo = random.randint(100,999) 
       


## Derived from payment process. Needs its own receipt because it did not inherit the print receipt from card payment
class cashPayment (paymentProcess):
  amountGiven = 0.0
  change = 0.0

  def setAmountGiven (self, a):
      self.amountGiven = a

  def calcChange (self):
      self.change = self.amountGiven - self.amount

  def __init__(self, custName, amount, given):
        self.setCustomerName(custName)
        self.setAmount(float(amount))
        self.setAmountGiven(int(given))
        self.calcChange()

  def printReceipt(self):
    print("\n\n\n\tReceipt")
    print("Name: " + self.customerName)
    print("Total: $%.2f" %(self.amount))
    print("Time: " + self.timeStamp)
    print("Change: $%.2f" %(self.change))
    print("\n\n")


## Function to print all the saved receipts
def printHistory():
    print("Credit Card Receipts: ")
    for i in range(0,len(creditHistory)):
        creditHistory[i].printReceipt()
    print("Debit Card Receipts: ")
    for i in range(0,len(debitHistory)):
        debitHistory[i].printReceipt()
    print("Cash Receipts: ")
    for i in range(0,len(cashHistory)):
        cashHistory[i].printReceipt()

## Simple function to print options to the user
def printMenu():
    print("1: Credit Card")
    print("2: Debit Card")
    print("3: Cash")
    print("4: Cancel\n")

## Initialize a payment function
## End goal of this function is to append a payment object to one of the 3 arrays keeping a history of payments
def startPayment(order):

    print("~~~~~~~~~~~~~~~~~~~~~~~\n\tPAYMENT\n~~~~~~~~~~~~~~~~~~~~~~~\n")

    subtotal = 0.0
    for i in range(0,len(order)):
        subtotal += (subtotal + (float(order[i].price) * float(order[i].quantity)))
    total = ((subtotal * 0.07) + subtotal)
    print("BILL\nItem\tPrice\tQuantity")
    for x in range(0,len(order)):
            print(order[x].itemName + "\t$" + str(order[x].price) + "\t" + str(order[x].quantity))
    print("\nSubtotal: $%.2f\n" %(subtotal))
    print("Total: $%.2f" %(total))
    print("\n\nChoose payment method\n")
    printMenu()

    choice = input()
    if (choice == "1"):
        tempName = input("Enter a name for the order: ")
        tempAmount = total
        tempZip = input("Enter Zip code: ")

        tempPayment = creditCard(tempName, tempAmount,tempZip)

        creditHistory.append(tempPayment)
        creditHistory[len(creditHistory)-1].printReceipt()

    # Do stuff for adding a credit card to history
    elif(choice == "2"):

        tempName = input("Enter a name for the order: ")
        tempAmount = total
        tempPin = input("Enter pin: ")
        debitHistory.append(debitCard(tempName, tempAmount, tempPin))
        debitHistory[len(debitHistory)-1].printReceipt()

        # Do stuff for adding a debit card to history
    elif(choice == "3"):
        
        tempName = input("Enter a name for the order: ")
        tempGiven = input("Enter amount received: $")
        if (float(tempGiven) >= total):
            print(total)
            cashHistory.append(cashPayment(tempName, total, tempGiven))
            cashHistory[len(cashHistory)-1].printReceipt()
            # Do stuff for adding cash transcation to history
        else:
            print("Insufficient amount given.")


    elif(choice == "4"):
        return
    
    else:
        print("Invalid input")


## Initialize 3 arrays to keep history of payments
creditHistory = []
debitHistory = []
cashHistory = []


## Create main function just to organize things better
def main(): 
    print("\tWELCOME!")
    userChoice = "0"
    while(userChoice != "3"):
        userChoice = input("1: Start new order\n2: Payment History\n3: Exit\nEnter Choice Here: ")
        if(userChoice == "1"):
            startPayment(createOrder())
        elif(userChoice == "2"):
            printHistory()
        elif(userChoice == "3"):
            exit()
        else:
            print("Invalid Input. Try Again")


main()