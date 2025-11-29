#defining a guess number function
secretNumber = 15
attempts=1 #attempts starts from 1
def guessNumber ():
    for number in range(1,20):
        while attempts <= 5:
            guess=int(input('guess the number: '))
            if guess== secretNumber:
                print('congrats you guessed it right')
                break # exit the game if guess is right
            elif guess > 20:
                print(f'The number {guess} is too high')
            elif guess < 5:
                print(f'The number {guess} is too low')
            else:
                print ('game over')
            attempts+=1 # attempts = attempts + 1
guessNumber()



