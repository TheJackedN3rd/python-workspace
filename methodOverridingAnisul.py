class Phone:
    def __init__(self):
        print("I am in phone class")
        
class Samsung(Phone): #Phone is the parent/base/superclass class and samsung is the child/subclass/derived class
    def __init__(self):
        super().__init__()
        print("I am in samsung class") #this is method overriding
        
s1 = Samsung()
