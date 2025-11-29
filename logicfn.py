# simulating login functionality
username = 'silv12'
password = '4822'
def login():
    my_username = input('Enter your username: ')
    my_password = input('Enter your password: ')
    if my_username == username and my_password == password:
        print('Login successfull')
    else:
        print('Either username and password do not match')

login()