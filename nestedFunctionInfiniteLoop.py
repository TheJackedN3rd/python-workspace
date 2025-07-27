def f():
    print("Inside F")
    def g():
        print("Inside G")
        f()
    g() #won't work if we call it directly as it is a nested function
    
f()


#limit crossed so functions won't call after a limit