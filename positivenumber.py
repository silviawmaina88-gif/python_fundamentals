def positiveNumbers():
    for number in range(-20,21):
        if number < 0:
            continue # skips numbers less than 0
        else:
            print(number)

# positiveNumbers()

def numbersAboveZero():
    for number in range(-20, 21):
        if number >= 0:
            print(number)

numbersAboveZero()