# local hospital record
num_of_patient= int(input('enter the number of patients:'))
patients={}
for k,v in patients.items():
    name=(f'k,enter patients name{k}:')
    temp=(f'v,enter patients temperature{v}:')
    avg_temp=(sum(temp))/2
    if temp == 38 :
        print('highest temperatute')
    elif temp == 20:
        print('lowest temperature')

