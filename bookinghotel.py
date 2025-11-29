# booking a hotel
charge_per_day = 500
def bookHotel():
    id_number = input('Enter your id number: ')
    first_name = input('Enter your first name: ')
    age = input('Enter your age: ')
    duration = int(input('Enter number of days to stay: '))
    total_amount = charge_per_day * duration
    print(f'Total amount to pay for {duration} days is: {total_amount}')
    print(f'Details confirmed: Id Number: {id_number}, Name: {first_name} , Age: {age}')
    print(f'Booking successful for {first_name} and payable amount is {total_amount}')

bookHotel()