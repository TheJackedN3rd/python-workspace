#higher order function is : A function that takes another function as input, or returns a function, or both.
#Two things make a function "higher order":It accepts a function as an argument.It returns a function as a result.
#If it does either, it’s officially a higher order function.

def return_sum(func,l):
    result = 0
    for i in l:
        if func(i):
            result = result + i
    return result
    
l = [11,12,14,15,34,23,13,78,53]
a = lambda x : x%2 == 0
b = lambda x : x%2 != 0
c = lambda x : x%3 == 0

print(return_sum(a,l))
print(return_sum(b,l))
print(return_sum(c,l))