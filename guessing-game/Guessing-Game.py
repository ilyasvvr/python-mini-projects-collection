import random

print('Welcome to the Number Guessing Game!')
difficulty = input('Choose difficulty: \n 1 - Easy \n 2 - Medium \n 3 - Hard \n > ')

if difficulty == '1':
    secret_number = random.randint(0, 100)
elif difficulty == '2':
    secret_number = random.randint(0, 1000)
elif difficulty == '3':
    secret_number = random.randint(0, 10000)
else:
    print('Invalid choice, setting to Easy.')
    secret_number = random.randint(0, 100)

attempts = 0

while True:
    guess = input('Enter your guess: ')

    if not guess.isdigit():
        print("Please enter a valid number!")
        continue

    guess = int(guess)
    attempts += 1

    if guess == secret_number:
        print(f'Congratulations! You guessed the number in {attempts} attempts!')
        break
    elif guess < secret_number:
        print('Too Low! Try a bigger number.')
    else:
        print('Too High! Try a smaller number.')
