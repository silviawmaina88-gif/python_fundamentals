# Restaurant discount system function
def discount():
    bill = int(input('Enter your bill amount: '))

    if bill > 1000:
        discount = bill * 0.10
        print('Your discount is:', discount)

    elif bill >= 500 and bill <= 1000:
        discount = bill * 0.05
        print('Your discount is:', discount)

    else: 
        print('No discount')

discount()