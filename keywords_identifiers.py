#python is a case sensitive language
#keywords are reserved words in python
#they cannot be used as variable names
#keywords are used to define the syntax and structure of the Python language

#python has 35 keywords

import keyword
print(keyword.kwlist)  # This will print the list of keywords in Python

#identifiers are names used to identify a variable, function, class, module, or other object
#they can be any length and can consist of letters, digits, and underscores

#identifiers must start with a letter or underscore, followed by letters, digits, or underscores
#identifiers are case sensitive, meaning that 'myVariable' and 'myvariable' are different identifiers
#identifiers cannot be the same as keywords

_ = 10  # This is a valid identifier, but using a single underscore is not recommended for general use

print(_)  # This will print the value of the identifier '_'

___ = 20  # This is also a valid identifier, but using multiple underscores is not recommended for general use

print(___)  # This will print the value of the identifier '___'