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

class Atm:
    def __init__(self): #This is the constructor method.It runs automatically every time you create a new Atm object.
        self.pin = ""
        self.balance = 0
        
        
        self.menu()
        
    def menu(self):
        pass