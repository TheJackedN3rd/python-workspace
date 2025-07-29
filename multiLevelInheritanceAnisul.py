#multilevel Inheritance

class A:
    def display1(self):
        print("I am inside of A class")
        
class B(A):
    #display1()
    def display2(self):
        print("I am inside of B class")
        
class C(B):
    #display1(),display2()
    def display3(self):
        super().display1()
        super().display2()
        print("I am inside of C class")
        
        
        
c = C()

c.display3()