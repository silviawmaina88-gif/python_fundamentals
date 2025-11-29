try:
    fnumber=int(input('enter first number: '))
    snumber=int(input('enter second_number: '))
    result=fnumber / snumber
    print(result)
except ZeroDivisionError:
    print('Either of the numbers cannot be zero')
except ValueError:
    print('Invalid input')
 