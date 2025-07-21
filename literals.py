#literals
#Literals are the raw data that you assign to variables
#They can be of various types such as integers, floats, strings, and booleans
#types of literals in Python
#1. Numeric literals
#2. Special literals
#3. String literals
#4. Boolean literals

#Numeric literals can be integers or floats
#Integer literals can be binary,decimal, octal, or hexadecimal

a = 10  # This is a decimal literal (base 10)
b = 0b10  # This is a binary literal (base 2)
c = 0o10  # This is an octal literal (base 8)
d = 0x12c  # This is a hexadecimal literal (base 16)

print(a, b, c, d)  # This will print the values of a, b, c, and d

#float literals can be written in decimal or scientific notation
e = 10.5  # This is a float literal in decimal notation
f = 1.5e2  # This is a float literal in scientific notation
g = 1.5e-2  # This is a float literal in scientific notation with a negative exponent

print(e, f, g)  # This will print the values of e, f, and g

#complex literals can be written with a real and imaginary part
h = 1 + 2j  # This is a complex literal with real part
i = 3.5 + 4.5j  # This is another complex literal with real and imaginary parts
print(h, i)  # This will print the values of h and i

print(i,i.real,i.imag)  # This will print the real and imaginary parts of the complex number i

#string literals can be written with single, double, or triple quotes
j = "Hello, World!"  # This is a string literal with double quotes
k = 'Hello, World!'  # This is a string literal with single quotes
l = '''This is a multi-line string.It can span multiple lines.'''  # This is a multi-line string with triple quotes
m = """This is another multi-line string.It can also span multiple lines."""  # Another multi-line string with triple quotes
print(j, k, l, m)  # This will print the values of j, k, l, and m
char = 'a'  # This is a character literal, which is also a string in Python
print(char)  # This will print the character 'a'
unicode = '\u03A9'  # This is a Unicode character literal for the Greek letter Omega
print(unicode)  # This will print the Unicode character Ω
raw_string = r"This is a raw string.\nIt does not interpret escape sequences."  # This is a raw string literal
print(raw_string)  # This will print the raw string without interpreting escape sequences

#boolean literals can be True or False
a = True + 5  # This will add 1 (True is treated as 1) to 5
b = False + 5  # This will add 0 (False is treated as 0) to 5
print(a, b)  # This will print the values of a and b

#Special literals in Python include None, which represents the absence of a value
a = None  # This is a special literal representing no value
print(a)  # This will print None, indicating no value assigned