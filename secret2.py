import random
# the number the user needs to guess
secret_number= random.randint(1,10)

#initialize the guess variable to a value that is not the secret number
guess=0
print("guess the secret number between 1 and 10:")

# the loop condition: condition running is a long as the guess is not correct
while guess !=secret_number:
    # get user input inside the loop
    user_input = input("enter your guess:")

    try:
        # convert input to an integer: 
        guess=int(user_input)

        # provide feedback to the user:
        if guess < secret_number:
            print("too low! try again.")
        elif guess > secret_number:
            print("too high! try again.")
        
    except ValueError:
        # handle non numeric input gracefully
        print ("invalid input,please enter a whole number.")

# this code runs only after the loop condition (guess != secret_number) becomes false
print("congratulations ! you guessed the number (secret_number) correctly.")
