def power(a,b):
    return a**b

print(power(2,5))

#another way :

#default_parameter

def power(a=1,b=1):
    return a**b

print(power(2,3))
print(power(2))

#positional arguments
#positions of a,b..order by order.

#keyword arguments
#overeides positional arguments

print(power(b=2,a=3)) #positional but we defined a,b

#Arbitary Arguments
#print(1,2,3,..)
#doesn't matter how much inputs you give

def flex(*number):
    product = 1
    for i in number:
        product = product * i
    return product
    

print(flex(1))
print(flex(1,2,3))


def flex(*number):
    product = 1
    print(number)
    print(type(number))
    for i in number:
        product = product * i
    return product

print(flex(1,2,3,4,5,6))