def f():
    print("Inside F")
    def g():
        print("Inside G")
    g() #won't work if we call it directly as it is a nested function
    
f()