#Abstraction and Decomposition in function

#Abstraction means hiding the complex details and showing only the essential features.When you call a function, you don't care how it works — only that it does.

#Decomposition is about breaking a big problem into smaller, manageable pieces — and solving each piece with its own function.

def is_even(n):
    """
    this Function tells if a given number is odd or even
    input - any int
    output - odd or even
    
    """
    if type(n) == int:
        if n % 2 == 0:   
            return "even"
        else:
            return "odd"
    else:
        return "not allowed"
    
for i in range(1,11):
    print(is_even(i))
    
print(is_even.__doc__)
print(is_even("Hello"))