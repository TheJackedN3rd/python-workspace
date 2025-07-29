#class is a blueprint
#object can be of a class
#data type is a class
#class has data/attribute/property and functions/behaviour/method
#name of the class should be in Pascal Case
#ThisIsPascalCase
#thisIsCamelCase
#snake_case
#data and function will be in snake_case
#object is an instance of a class

#a = 2
#print(type(a)) #a is a object of int class

#functions vs #Methods
#Method is a special function that is written inside a class
#len(L) this is a function.string,list anyone can use this
#L.append() this is a method inside list class.only object of a list class can use this

class ATM:
    def __init__(self): #This is the constructor method.It runs automatically every time you create a new Atm object.
        self.pin = ""
        self.balance = 0
        
        #self.menu()
        
    def menu(self):
        while True:
            user_input = input("""
                           Hello how would you like to proceed?
                           1. Enter 1 to create pin
                           2. Enter 2 to deposit
                           3. Enter 3 to withdraw
                           4. Enter 4 to check balance
                           5. Enter 5 to exit
                           """)
        
            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposite()
            elif user_input == "3":
                self.withdraw()
            elif user_input == "4":
                self.check_balance()
            elif user_input == "5":
                print("Exit")
            else:
                print("Bye")
            
    def create_pin(self):
        self.pin = input("Enter your pin")
        print("Pin created successfully")
        
    def deposite(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter the amount"))
            self.balance = self.balance + amount
            print("Deposit Successful.New Balance is",self.balance)
        else:
            print("Invalid Pin")
            
    def withdraw(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter the amount"))
            if amount < self.balance:
                self.balance = self.balance - amount
                print("Withdraw Successful.New Balance is",self.balance)
            else:
                print("You don't have enough balance")
        else:
            print("Invalid Pin")
                
    def check_balance(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            print("Your balance is",self.balance)
        else:
            print("Invalid Pin")