c = "hello world"

print(c)
print(len(c))  # Length of the string

print(max(c))  # Maximum character in the string
print(min(c))  # Minimum character in the string

print(sorted(c))  # Sorted list of characters in the string
print(sorted(c, reverse=True))  # Sorted list of characters in reverse order

print(c.capitalize())  # Capitalizes the first character
print(c.title())  # Capitalizes the first character of each word
print(c.upper())  # Converts the string to uppercase
print(c.lower())  # Converts the string to lowercase
print(c.swapcase())  # Swaps the case of each character

print(c.count('l'))  # Counts the occurrences of 'l'
print(c.count('hello'))  # Counts the occurrences of 'hello'
print(c.find('l'))  # Finds the first occurrence of 'l'
print(c.find('x'))  # Returns -1 if 'x' is not found
print(c.index('l'))  # Finds the first occurrence of 'l' (raises error if not found)
#print(c.index('x'))  # Raises ValueError if 'x' is not found

print(c.endswith('world'))  # Checks if the string ends with 'world'
print(c.startswith('hello'))  # Checks if the string starts with 'hello'

print("{} my {}".format("Hello","World"))  # Formats the string (no placeholders to replace)
print("{1} my {0}".format("Hello","World"))
print("{greet} my {G}".format(greet = "Hello",D = "World",G = "Cox"))

print(c.isalnum())  # Checks if all characters are alphanumeric
print(c.isalpha())  # Checks if all characters are alphabetic

print(c.isdigit())  # Checks if all characters are digits
print(c.isidentifier())  # Checks if the string is a valid identifier

print(c.split())  # Splits the string into a list of words
print(c.split('o'))  # Splits the string at 'o'
print(c.split('l'))  # Splits the string at 'l'


print('/'.join(c.split()))  # Joins the list of words with a slash

print(c.replace('l', 'x'))  # Replaces 'l' with 'x'
print(c.replace('hello', 'hi'))  # Replaces 'hello' with 'hi'
print(c.replace('x', 'y'))  # Replaces 'x' with 'y

a = "          Hello World      "
print(a)  # Original string with leading and trailing spaces 
print(a.strip())  # Removes leading and trailing whitespace
print(a.lstrip())  # Removes leading whitespace
print(a.rstrip())  # Removes trailing whitespace