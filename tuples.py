#tuples vs lists
# Lists are mutable, meaning they can be changed after creation.
# Tuples are immutable, meaning they cannot be changed after creation.
#tuples are read only


t1 =()  # Empty tuple
print("Empty Tuple:", t1)

t2 = (1, 2, 3)  # Tuple with integers
print("Tuple with integers:", t2)

t3 = (1, 2.5, "Hello", True)  # Tuple with mixed data types
print("Tuple with mixed types:", t3)

t4 = (1, 2, 3, [4, 5, 6])  # Tuple with a list inside
print("Tuple with a list:", t4)

t5 = (1)  # This is not a tuple, it's just an integer
print("Not a tuple:", t5)
print("Type of t5:", type(t5))

t6 = (1,)  # This is a tuple with one element
print("Tuple with one element:", t6)
print("Type of t6:", type(t6))  # This will show it's a tuple

t6 = tuple("Hello")  # Convert string to tuple of characters
print("Tuple from string:", t6)

t7 = tuple([1, 2, 3])  # Convert list to tuple
print("Tuple from list:", t7)

print(t2[0])

print(t2[:2])  # Slicing the tuple

print(t4[3][1])  # Accessing an element in the list inside the tuple

#t2[0] = 10  # This will raise an error because tuples are immutable

del t2  # Deleting the tuple
print("Tuple t2 deleted.")

#del t4[3][1]  # This will not raise an error because we are modifying the list inside the tuple

for i in t3:
    print("Element in t3:", i)
    
    
print("Length of t3:", len(t3))  # Length of the tuple
#print(max(t3))  # Maximum value in the tuple

