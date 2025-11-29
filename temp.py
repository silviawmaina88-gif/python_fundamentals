temperature = int(input('Enter value: '))
if temperature < 15:
    print('Cold')
elif temperature > 15 and temperature <= 30:
    print('Moderate')
elif temperature > 30:
    print('Hot')