#operations on strings




#Membership Operations

#Arithmetic Operations

c = "Hello" + "World"
print(c)

print("Hello" * 3)  # Repeating the string 3 times
print(c * 2)  # Repeating the string c twice

#Relational Operations

"hello" == "Hello"  # False, case-sensitive comparison
"hello" != "Hello"  # True, case-sensitive comparison
"hello" < "Hello"  # False, based on lexicographical order
"hello" > "Hello"  # True, based on lexicographical order

#Logical Operations

print("Hello" and "World")  # Returns "World", the second operand
print("Hello" or "World")  # Returns "Hello", the first operand

print("Hello" and "")  # Returns "", the second operand is empty
print("" or "World")  # Returns "World", the first operand is empty

print(not "Hello")  # Returns False, since "Hello" is truthy
print(not "")  # Returns True, since an empty string is falsy

#Loops on strings

for i in c:
    print(i)  # Prints each character in the string c
    
for char in c[::2]:  # Slicing with a step of 2
    print(c)  # Prints every second character in the string c
    
print('hello' in c)  # Checks if 'hello' is a substring of c
print('Hello' in c)  # Checks if 'Hello' is a substring of c