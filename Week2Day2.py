import random
def generate_number():
    return random.randint(1, 100)
def get_guess():
    guess = int(input("Guess a number between 1 and 100: "))
    return guess
def check_guess(secret_number, guess):
    if guess < secret_number:
        print("Higher.")
        return False
    elif guess > secret_number:
        print("Lower.")
        return False
    else:
        print("Correct!")
        return True
def main():
    secret_number = generate_number()
    attempts = 0
    while True:
        guess = get_guess()
        attempts += 1
        if check_guess(secret_number, guess):
            print("You guessed it in", attempts, "attempts.")
            break
main()