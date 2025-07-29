#"How many pairs of rabbits will be produced in a year, beginning with a single pair, if every pair produces a new pair every month starting from the second month?"

#The Rules:
#You start with 1 pair of baby rabbits.
#Rabbits take 1 month to mature.\
#Every mature pair produces 1 new pair of rabbits every month.

def fib(m):
    if m==0 or m==1:
        return 1
    else:
        return fib(m-1) + fib(m-2)
    
    
print(fib(5)) #Too much time complexity as many fib will be calculated twice.