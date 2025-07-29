class Phone:
    def call(self):
        print("you can call")
    def message(self):
        print("you can message")
        
class Samsung(Phone): #Phone is the parent/base/superclass class and samsung is the child/subclass/derived class
    #call,message
    def photo(self):
        print("you can take photos")
        
p1 = Phone()
p1.message()
p1.call()

s1 = Samsung()
s1.message()
s1.call()
s1.photo()

print(issubclass(Samsung,Phone))
print(issubclass(Phone,Samsung))