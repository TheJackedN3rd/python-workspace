#constructor is used to initialize an object

class Student:
    roll = ""
    gpa = ""
    
    def __init__(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa
        
    def display(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")
    
rahim = Student(102,3.75)
rahim.display()


karim = Student(101,3.45)
karim.display()