#function without a name
#works with a single line of code
#lambda has no return value,it returns the whole function
#lambda can write not more than one line
#it's for one time use,not for code reusability
#lambda is used along with higher order functions
#lambda parameter : expression

#def cal(a,b):
#    return a*a + 2*a*b + b*b

#print(cal(4,5))

#print((lambda a,b : a*a + 2*a*b + b*b) (2,3))

a = lambda x : x**2
print(a(9))
print(type(a))

b = lambda x,y : x+y
print(b(4,5))
print(type(b))

c = lambda x : x[0] == 'a'
print(c('apple'))
print(c('mapple'))

d = lambda x: "Even" if x%2 == 0 else "odd"
print(d(34578923457890))