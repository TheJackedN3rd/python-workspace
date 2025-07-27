#Mutalbility refers to the ability to change or edit data in it's memory location

a = "hello"
print(id(a))

a = a + "World"
print(id(a))

a = (1,2,4)
print(id(a))

a = a + (4,5)
print(id(a))

#mutable data type

a = [1,2,3]
print(id(a))
a.append(4)
print(id(a))

L = [1,2,3]
L1 = L
print(L1)
print(L)
print(id(L1))
print(id(L))
L1.append(4)
print(L1)
print(L)
print(id(L1))
print(id(L))

L = L + [4,5]
print(id(L))

L1 = L[:] #copy L1 in a different memory address

print(id(L1))
print(id(L))

a = (1,2,3,[4,5])
a[-1][-1] = 500 #as list is mutable even though tuple is immutable
print(a)

a = [1,2,3,(4,5)]
#a[-1][-1] = 500 #won't work as tuple is immutable even though list is mutable

a = [1,2]
b = [3,4]
c = (a,b)

print(c)

print(id(a))
print(id(b))
print(id(c))

c [0][0] = 100
print(c)

a = a + [5,6]
print(c)

#c[0] = c[0] + (5,6)


L = [1,2,3]
print(id(L))
L = L + [4,5] #concatanation makes a new list
print(id(L))
