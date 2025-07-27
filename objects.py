#Everything is in python is an object.Even Function is an object too

#In Python, literally everything — numbers, strings, functions, even classes — is an object.And by “object,” we mean: it’s an instance of some class and has attributes and methods.

#if functions are objects, you can:

#Pass them as arguments to other functions

#Store them in data structures

#Assign them to variables

#Return them from other functions

def f(n):
    return n**2

print(f(2))
print(f(5))

x = f #function aliasing
print(x(3))

del f
print(x(6))

print(type(x))

L = [1,2,3,4,x]
print(L)

print(L[-1](9))

L1 = [1,2,3,4,x(5)]
print(L1)

