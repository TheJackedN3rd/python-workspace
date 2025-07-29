#magic methods start with __

class Student:
    roll = ""
    gpa = ""
    
    def __eq__(self, other):
        return self.roll == other.roll and self.gpa == other.gpa
    
    def __init__(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa
       
    def __str__(self):
        return f"Roll : {self.roll}, GPA : {self.gpa}"
         
    def display(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")
    
rahim = Student(101,3.45)
print(rahim)


karim = Student(101,3.45)
print(karim)

print(rahim == karim)