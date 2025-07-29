#A function that calls itself is said to be recursive, and the technique of employing a recursive function is called recursion.

def mul(a,b):
    return a*b

print(mul(5,6))


def mult(a,b):
    r = 0
    for i in range(b):
        r = r + a
        
    print(r)
    
mult(5,6)


def multiply(a,b):
    if b == 0:
        return 0   
    elif b == 1:
        return a
    else:
        return a + multiply(a,b-1)
    
    
print(multiply(7,8))