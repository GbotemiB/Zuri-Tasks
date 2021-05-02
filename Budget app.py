
database = {"food":2000}

class Budget:

    def __init__(self, category):
        #initialise cash to 0
        cash = 0

        self.category = category
        self.cash = cash 
    
    def withdraw(categoryName, amount):
        amountInStock = database[categoryName]
        amountInStock -= amount
        database[categoryName] = amountInStock
        print(f"your budget balance is {amountInStock}")
    
    def deposit(categoryName, amount):
        amountInStock = database[categoryName]
        amountInStock += amount
        database[categoryName] = amountInStock
        print (f"your budget balance is {amountInStock}")


    def categoryBalances():
        for data, items in database.items():
            print (f"Balance for {data} is {items}")
        

    def transferBalance(category1, amount, category2):
        withdrawn = database[category1]
        sent = database[category2]

        database[category1] = withdrawn - amount
        database[category2] = sent + amount
        return database

    def newCategory(createCategory):
        try:
            createBudgetAmount = int(input("Please Deposit any amount into your Category \n"))
            database[createCategory] = createBudgetAmount
            print (database)
        except ValueError:
            print("Amount must be an integer")
            Budget.newCategory(createCategory)
    

    
def start():
    print ("Welcome to the Budget App")
    print ("=============================")
    toDo()

def toDo():
    try:
        todo = int(input("What will you like to do \n(1) Create a new budget category \n(2) Deposit funds into a Budget \n(3) Withdraw funds from a budget \n(4) See budget balances \n(5) Transfer balance between budget \n(6) Exit\n"))
        if (todo == 1):
            createBudget()
            otherActions()
        elif todo == 2:
            depositFunds()
            otherActions()
        elif todo == 3:
            withdrawFunds()
            otherActions()
        elif todo == 4:
            budgetBalance()
            otherActions()
        elif todo == 5:
            transferBalance()
            otherActions()
        elif todo == 6:
            print("thank you for using the budget app")
            exit()
        else:
            print ("Invalid option, please try again")
            toDo()
    except ValueError:
        print("Option must be an integer")
        toDo()

def createBudget():
    name = input("please enter category name\n")
    if name not in database.keys():
        Budget.newCategory(name)
    else:
        print("Category already exists, try again.")
        createBudget()

def depositFunds():
    category = input("what is the name of the category you want to deposit funds into? \n")
    if category in database.keys():
        isTrue = True
        while isTrue == True:
            try:
                amount = int(input("How much will you like to deposit? \n"))
                Budget.deposit(category, amount)
                isTrue = False

            except ValueError:
                print("option must be integer")
    else:
        print("Please enter a correct category")
        depositFunds()

def withdrawFunds():
    category = input("what is the name of the category you want to withdraw funds from? \n")
    if category in database.keys():
        isFalse = False
        while isFalse == False:
            try:
                amount = int(input("How much will you like to withdraw? \n"))
                Budget.withdraw(category, amount)
                isFalse = True
            except ValueError:
                print("option must be an integer")

    else:
        print("Please enter a correct category")
        withdrawFunds()

    

def budgetBalance():
    Budget.categoryBalances()

def transferBalance():
    category1 = input("enter category you want to transfer from? \n")
    if category1 in database.keys():
        isFalse = False
        while isFalse == False:
            try:
                amount = int(input("Enter the amount you want to transfer \n"))
                category2 = input("enter category you want to transfer to \n")
                if category2 in database.keys():
                    Budget.transferBalance(category1, amount, category2)
                else:
                    print("ensure the category exists")
                    transferBalance()
                isFalse = True
            except ValueError:
                print("amount must be an integer")
        
    else:
        print("ensure you the category exists")
        transferBalance()

def otherActions():
    try:
        Input = int(input("Will you like to perform other actions (1) yes (2) no \n"))
        if Input == 1:
            toDo()
        elif Input == 2:
            print("thank you for using the budget app")
            exit()
        else:
            print ("please enter the right options")
            otherActions()
    except ValueError:
        print("options must be an integer")
        otherActions()


start()
