#solving with memorization
#Memoization is basically a smart remembering technique. Instead of recalculating the same stuff over and over (which is exactly what happens with the naive Fibonacci recursion), you store the results of expensive function calls and reuse them when the same inputs occur again. It’s like writing down answers to tricky questions so you don’t have to solve them again
#You’re trying to find Fibonacci of 50. The naive method calls Fibonacci(49) and Fibonacci(48). Then Fibonacci(49) calls Fibonacci(48) and Fibonacci(47). Notice Fibonacci(48) is calculated twice? And this repeats exponentially.Memoization says, “Hold up, I already did Fibonacci(48), lemme just grab the answer from the notebook.”
import time
def memo(n,d):
    if n in d:
        return d[n]
    else:
        d[n] = memo(n-1,d) + memo(n-2,d)
        return d[n]
    
start = time.time()
d = {0:1,1:1}
print(memo(48,d))
print(time.time()-start)
print(d)
