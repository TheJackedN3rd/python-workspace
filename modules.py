#modules

#help("modules")

import math

print(math.pi)
print(math.sqrt(16))  # Square root of 16
print(math.factorial(5))  # Factorial of 5
print(math.pow(2, 3))  # 2 raised to the power of 3
print(math.gcd(12, 15))  # Greatest common divisor of 12 and 15
print(math.sin(math.pi / 4))  # Sine of 90 degrees
print(math.e)  # Euler's number
print(math.ceil(4.2))  # Ceiling of 4.2
print(math.floor(4.8))  # Floor of 4.8

import random

print(random.randint(1, 10))  # Random integer between 1 and 10
print(random.choice(['apple', 'banana', 'cherry']))  # Random choice from a list
print(random.sample([1, 2, 3, 4, 5], 3))  # Random sample of 3 elements from a list
print(random.uniform(1.0, 10.0))  # Random float between 1.0 and 10.0

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)  # Shuffle a list in place
print(my_list)

import time

print(time.time())  # Current time in seconds since the epoch
print(time.ctime())  # Current time in seconds since the epoch
print(time.localtime())  # Current local time

print("hello world")
print(time.sleep(2))  # Sleep for 2 seconds
print("hello again")

import os
print(os.getcwd())  # Get current working directory
print(os.listdir('.'))  # List files in the current directory