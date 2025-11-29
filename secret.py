secret_number = 8 # secrete number to refer from
attempts = 1 # number of sttempts starts from 1 
while attempts <= 3: # maximum number of attempts is 3
    guess = int(input('Gues your number ')) # get number from user
    if guess == secret_number: # condition is checked
        print('You won')
        break # stop when the guess is right
    else:
        print('Try again') # guess again
    attempts = attempts + 1

# pin = 5567
# attempts = 1