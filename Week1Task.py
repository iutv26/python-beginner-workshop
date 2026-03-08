import random
number = random.randint(1, 100)
attempts = 0
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1
    if guess < number:
        print("Higher")
    elif guess > number:
        print("Lower")
    else:
        print("Correct!")
        print("You guessed it in", attempts, "attempts")
        break