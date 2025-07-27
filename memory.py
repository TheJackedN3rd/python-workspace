##python calls variable as "name"
#
#a = 4
#print(id(a))
#print(hex(id(a)))
#
#print(type(id(a)))
#
#print(id(4))
#
##aliasing
#
#a = 5
#b = a
#print(id(a))
#print(id(b))
#del(a)
#print(id(b))
#
#a = 5
#b = a
#a = 6
#print(a)
#print(b)
#
#import sys
#b = 'corona'
#b = a
#c = b
#print(id(a))
#print(id(b))
#print(id(c))
#
#print(sys.getrefcount(a))
#
##Garbage Collection
##Weird Behaviour
#
#a = 613
#print(sys.getrefcount(a))
#b = a
#c = b
#
#print(sys.getrefcount(a)) #2 ke oneke use kortese tai eto boro value.
#
#print(id(a))
#print(id(b))
#
#a = 266
#b = 266
#
#print(id(a))
#print(id(b))
#
#a = "obd"
#b = "obd"
#print(id(a))
#print(id(b))
#
#a = "obd boss cox king"
#b = "obd boss cox king"
#print(id(a))
#print(id(b))
#
#
L = [1,2,3]
print(id(L))
print(id(L[0]))
print(id(1))
print(id(L[1]))
print(id(2))
print(id(L[2]))
print(id(3))


