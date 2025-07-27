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