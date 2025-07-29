import time
def fib(m):
    if m==0 or m==1:
        return 1
    else:
        return fib(m-1) + fib(m-2)
    
start = time.time()
print(fib(5))
print(time.time()-start)

print(fib(12))
print(time.time()-start)

print(fib(24))
print(time.time()-start)

print(fib(36))
print(time.time()-start)

print(fib(37))
print(time.time()-start)

print(fib(38))
print(time.time()-start)

#time is growing exponentially so the code is not usable for large numbers
#also the code is going to repeat many fib number calculations so it is not efficient