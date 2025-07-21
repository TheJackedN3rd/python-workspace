#strings are sequences of characters
#in python, strings are sequences of unicode characters

a = "Hello"
print(a)
a = 'Hello'
print(a)
a = '''Hello'''#multiline string
print(a)
a = """Hello"""#multiline string
print(a)

print("It's a beautiful day")

c = str("Hello World")
print(c)

print(c[0])  # Accessing the first character
print(c[1])  # Accessing the second character
print(c[4])  # Accessing the fifth character
print(c[-1])  # Accessing the last character  
print(c[-5]) # Accessing the first character using negative indexing

print(c[0:2])  # Slicing from index 0 to 1
print(c[1:4])  # Slicing from index 1 to 3

print(c[2:])   # Slicing from index 2 to the end
print(c[:5])   # Slicing from the start to index 4

print(c[:])# Full string
print(c[::2])  # Slicing with a step of 2
print(c[::-1])  # Reversing the string 
print(c[1:10:2])  # Slicing with a step of 2 from index 1 to 9

print(c[-5:-1:2])  # Slicing with a step of 2 from index -5 to -2

c = "Hello World"
print(c)

del c  # Deleting the string variable
print(c)  # This will raise an error since c is deleted

c = "Hello World"
del c[0]  # This will raise an error since strings are immutable