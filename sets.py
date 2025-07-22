#sets
#sets do not allow duplicates
#sets have no indexing
#sets dont allow mutable data types
#sets itself is a mutable data type
#sets are unordered
#2d sets are not possible
#sets are defined using curly braces or the set() constructor
#sets can be used to remove duplicates from a list
#sets can be used to perform mathematical set operations like union, intersection, and difference
#hashing is used to store sets in memory, which allows for fast membership testing


s1 = {}
print(type(s1))  # <class 'dict'>, this is a dictionary, not a set

s1 = set()
print(type(s1))  # <class 'set'>, this is a set

s1 = {1, 2, 3, 4, 5}
print(s1)  # {1, 2, 3, 4, 5}

s2 = {1, 2, 3, 4, 5, 5}  # duplicates are removed
print(s2)  # {1, 2, 3, 4, 5}

s3 = {1, 2, 3, 4, 5, 'a', 'b', 'c'}  # sets can contain mixed data types
print(s3)  # {1, 2, 3, 4, 5, 'a', 'b', 'c'}

#s4 = {"hello", [1, 2]} # sets cannot contain mutable data types like lists or dictionaries
#print(s4)

s4 = {"Hello", (1, 2)}  # sets can contain immutable data types like tuples
print(s4)  # {'Hello', (1, 2)}

#s5 = {{1, 2}, {3, 4}}  # sets cannot contain other sets
#print(s5)  # TypeError: unhashable type: 'set'

#print(s3[2])  # TypeError: 'set' object is not subscriptable, sets do not support indexing

print(id(s3))  # memory address of the set

l = list(s3)  # convert set to list
print(l)  # [1, 2, 3, 4, 5, 'a', 'b', 'c'] 
l[0] = 100  # modify the list
print(l)  # [100, 2, 3, 4, 5, 'a', 'b', 'c']
s3 = set(l)  # convert list back to set

s3.add(6)  # add an element to the set
print(s3)  # {1, 2, 3, 4, 5, 'a', 'b', 'c', 6}
print(id(s3))  # memory address of the set after modification

del s1  # delete the set

s3.remove(100)  # remove an element from the set
print(s3)  # {1, 2, 3, 4, 5, 'a', 'b', 'c', 6}

s3.pop()  # remove and return an arbitrary element from the set
print(s3)  # {2, 3, 4, 5, 'a', 'b', 'c', 6}

s7 = {1, 2, 3}
s8 = {3, 4, 5}
print(s7.union(s8))  # {1, 2, 3, 4, 5}  # union of two sets
print(s7 | s8)  # {1, 2, 3, 4, 5}  # union using the | operator
print(s7.difference(s8))  # {1, 2}  # difference of two sets
print(s7.symmetric_difference(s8))  # {1, 2, 4, 5}  # symmetric difference of two sets
print(s7 - s8)  # {1, 2}  # difference using the - operator
print(s7)
print(s7.intersection(s8))  # {3}  # intersection of two sets
print(s7 & s8)  # {3}  # intersection using the & operator
print(s7.isdisjoint(s8))  # False, the sets have common elements
print(s7.issubset(s8))  # False, s7 is not a subset of s8
print(s8.issubset(s7))  # False, s8 is not a subset of s7
print(s7.issuperset(s8))  # False, s7 is not a superset of s8
print(s8.issuperset(s7))  # False, s8 is not a superset of s7

print(len(s3))  # length of the set
print(3 in s3)  # True, check if an element is in the set  
print(100 in s3)  # False, check if an element is in the set
print(sorted(s7))  # ['a', 'b', 'c', 1, 2, 3, 4, 5, 6]  # sorted list of the set elements