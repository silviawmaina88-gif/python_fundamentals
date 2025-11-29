def largestNumber():
    a= int(input('enter first number:'))
    b= int(input('enter second number:'))
    c= int(input('enter third number:'))
    if a >=b and a>=c :
      print (f'largest is {a}')
    elif b >=a and b>=c :
        print(f'largest is {b}')
    
    else:
        print(f'largest is {c}')

largestNumber()

    


        
    