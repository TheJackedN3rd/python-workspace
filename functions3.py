def f(y):
    x = 1 #local variable(Exists only inside the function. Doesn't affect the outside world.)
    x = x + 1
    print(x) #2
    
x = 5 #Global Variable
f(x)
print(x) #global variable

