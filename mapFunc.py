#map(func, iterable) applies the function func to each item of the iterable (like a list), and returns a map object (which you usually turn into a list or other container).
#Think of it like this:
#Input: a list of data
#Tool: a function
#Output: a new list where every item has been transformed by that function
#Imagine you're running a factory line.
#You have a box of raw fruits: ["apple", "banana", "cherry"]
#You hand each fruit to a worker (func) that slices it in half.
#The map() function gives you a new box with all fruits halved.

#def sq(x):
#    return x*x
#
#l = [1,2,3,4,5]
#
#result = list(map(sq,l))
#print(result)


l = [1,2,3,4,5]
print(list(map(lambda x:x**2,l)))


print(list(map(lambda x:x%2==0,l)))