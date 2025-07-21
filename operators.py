#operators

#Arithmetic Operators

x = 10
y = 4
print("Addition:", x + y)  # Addition
print("Subtraction:", x - y)  # Subtraction
print("Multiplication:", x * y)  # Multiplication
print("Division:", x / y)  # Division
print("Floor Division:", x // y)  # Floor Division
print("Modulus:", x % y)  # Modulus
print("Exponentiation:", x ** y)  # Exponentiation

#Comparison Operators

print(x>y)  # Greater than
print(x<y)  # Less than
print(x>=y)  # Greater than or equal to
print(x<=y)  # Less than or equal to
print(x==y)  # Equal to
print(x!=y)  # Not equal to

#Logical Operators
x = True
y = False

print("Logical AND:", x and y)  # Logical AND
print("Logical OR:", x or y)  # Logical OR
print("Logical NOT:", not x)  # Logical NOT

#Bitwise Operators

x = 10  # Binary: 1010
y = 4   # Binary: 0100
print("Bitwise AND:", x & y)  # Bitwise AND
print("Bitwise OR:", x | y)  # Bitwise OR
print("Bitwise XOR:", x ^ y)  # Bitwise XOR
print("Bitwise NOT:", ~x)  # Bitwise NOT
print("Left Shift:", x << 1)  # Left Shift
print("Right Shift:", x >> 1)  # Right Shift

#assignment Operators
x = 10
y = 5
x += y  # x = x + y
print("After += :", x)  # x is now 15
x -= y  # x = x - y
print("After -= :", x)  # x is now 10
x *= y  # x = x * y
print("After *= :", x)  # x is now 50
x /= y  # x = x / y
print("After /= :", x)  # x is now 10.0
x //= y  # x = x // y
print("After //= :", x)  # x is now 2.0
x %= y  # x = x % y
print("After %= :", x)  # x is now 2.0
x **= y  # x = x ** y
print("After **= :", x)  # x is now 32.0

#Identity Operators

a = 3
b = 3

print("a is b:", a is b)  # True, as both refer to the same object
print("a is not b:", a is not b)  # False, as both refer to the same object

a= "Hello"
b = "hello"
print("a is b:", a is b)  # False, as both refer to different objects
print("a is not b:", a is not b)  # True, as both refer to different objects

a = [1, 2, 3]
b = [1, 2, 3]
print("a is b:", a is b)  # False, as both are different lists

a = "Hello"
b = "Hello"
print("a is b:", a is b)  # True, as both refer to the same string object in memory

a = "hello_world"
b = "hello_world"
print("a is b:", a is b)  # True, as both refer to the same string object in memory

#membership Operators
list1 = [1, 2, 3, 4, 5]
print("1 in list1:", 1 in list1)  # True, as 1 is in the list
print("6 in list1:", 6 in list1)  # False, as 6 is not in the list
print("1 not in list1:", 1 not in list1)  # False, as 1 is in the list