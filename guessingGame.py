import random
jackpot = random.randint(1, 100)
print("Welcome to the Guessing Game!")
guess = int(input("Guess a number between 1 and 100: "))
counter = 1
while guess != jackpot:
    if guess < jackpot:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
        
    guess = int(input("Guess a number between 1 and 100: "))
    counter += 1
    
print("Correct!")
print (f"You guessed the number {jackpot} in {counter} tries.")