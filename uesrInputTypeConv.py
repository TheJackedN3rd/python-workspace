# uesrInput.py
# This script takes user input and performs operations on it

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

print("You entered:", num1, "and", num2)
result = num1 + num2 # This will concatenate the strings
print("Concatenated result:", result)

# Note: To perform arithmetic operations, you need to convert the input to integers or floats

print(type(num1))# This will show the type of num1, which is str by default

#type conversion
#implicit conversion

print(type(4 + 5.5))  # This will show <class 'float'> due to implicit conversion
print(type(4 + 5 + 5j))  # This will show <class 'complex'> due to implicit conversion

#explicit conversion
num1 = int(num1)  # Convert num1 to integer
num2 = int(num2)  # Convert num2 to integer
result = num1 + num2  # Now this will perform arithmetic addition
print("Sum of numbers:", result)  # This will print the sum of num1 and num2
print(type(num1))  # This will show <class 'int'> after conversion
print(type(result))  # This will show <class 'int'> after addition

print(list("hello"))  # This will convert the string "hello" to a list of characters

a = 4.5
print(int(a))  # This will convert float to int, resulting in 4
print(a)
