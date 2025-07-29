#multilevel Inheritance

class A:
    def display(self):
        print("I am inside of A class")
        
class B:
    #display1()
    def display(self):
        print("I am inside of B class")
        
class C(A,B):
    pass
        
        
        
c = C()

c.display()