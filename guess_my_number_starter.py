import random
num = random.randint(1, 99)
guess = None


while guess != num:
    guess = input('Guess a number between 1 and 99: ')
    guess = int(guess)

    if guess == 94:
        print('Congratulations! You won, the number was: 94.')
        break
    elif guess > 94:
        print('Try again, your guess is too high!')
    else:
        print('Try again, your guess is too low!')