import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Ask the user to guess until they get it right
while True:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it right.")
        break
