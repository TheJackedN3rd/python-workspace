class Student:
    roll = ""
    gpa = ""
    
    def set_Value(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa
        
    def display(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")
    
rahim = Student()
print(isinstance(rahim,Student))

rahim.set_Value(101,3.45)
rahim.display()


karim = Student()
karim.set_Value(102,3.75)
karim.display()