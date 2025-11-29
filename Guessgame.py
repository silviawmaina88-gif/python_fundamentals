import random
def guess_number():
    secret = random.randint(1, 20)
    print('I\'m thinking of a number between 1 and 20.')
    for attempt in range(1, 6):
        try:
            guess = int(input(f'Attempt {attempt}: Enter your guess → '))
            if guess == secret:
                print('🎉 Congratulations! You guessed it right!')
                break
            elif guess < secret:
                print('Too low! Try again.')
            else:
                print('Too high! Try again.')
        except ValueError:
            print('Invalid guess')
    else:
        print(f'Game over! The number was {secret}.')

guess_number()