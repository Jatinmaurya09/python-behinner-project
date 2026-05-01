import random

low = 1
high = 100
attempt = 0

number = random.randint(low, high)

print("Guess the number between 1 and 100")

while True:
    guess = int(input("Enter number: "))
    attempt += 1

    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        score = max(100 - (attempt - 1) * 10, 0)
        print("Congratulations! You guessed correctly.")
        print(f"Attempts: {attempt}")
        print(f"Score: {score}")
        break