# a dictonary storing maedicine data
medicine = {
    'paracetamol': {'stock' :50,'price' :20},
    'amoxicillin': {'stock': 30,'price': 50},
    'ibuprofen' : {'stock': 40,'price' : 35}

}
# custom excemptions
class insufficientstockerror(Exception):
     """Raised when quantity is greater than available stock."""
     pass
class medicinenotfounderror (Exception):
     """Raised when medicine is not found."""
     pass
class nonnumericquantities (Exception):
     """Raised for invalid input types."""
     pass
# displaying the medicine
def view_medicine ():
        print('\n==current inventory==')
        for name, data in medicine.items():
            print(f"{name}: stock ={data['stock']},price =ksh {data['price']}")

    # adding stock

def add_new_medicine ():
        name= input("enter name of the medicine :").lower()
        if name in medicine:
         print('medicine already exist')
         return
        try:
              stock=int(input("enter stock quantity:"))
              price =float(input("enter price :"))
              medicine[name] = {'stock':stock,'price':price}
              print(f'added{name} succesfully !')
        except ValueError :
              raise nonnumericquantities("invalid input type for stock and price")

    # removing from stock

def sell_medicine ():
        name= input("enter name of the medicine :").lower()
        if name not in medicine:
              raise medicinenotfounderror("medicine not found.")
        try:
              quantity = int(input("enter quantity to sell:"))    
              if medicine[name]['stock'] < quantity :
                raise insufficientstockerror("not enough stock available.")
              medicine[name]['stock'] -= quantity
              total = medicine[name]['price'] * quantity
              print(f"sold{quantity} {name}(s). total =ksh {total}")
        except ValueError :
              raise nonnumericquantities ("quantity must be numeric")
        
            
def add_stock():
        name= input("enter name of the medicine :").lower()
        if name not in medicine:
               raise medicinenotfounderror("medicine not found")
        try :
               quantity = int(input("enter quantity to add:")) 
               medicine[name]['stock']+=quantity
               print(f'added {quantity} unit to{name}.')
        except ValueError :
                raise nonnumericquantities (("quantity must be numeric"))
#menu loop
while True:
    print('\n==pharmacy menu==')
    print('1. view medicine')
    print('2. add new medicine')
    print('3. sell medicine')
    print('4. add stock')
    print('5. Exit application')

    choice=input('enter your choice:')

    try:
        if choice =='1':
            view_medicine()
        elif choice=='2':
            add_new_medicine()
        elif choice =='3':
            sell_medicine()
        elif  choice=='4':
            add_stock()
        elif  choice == '5':
            print('Existing system ,Goodbye!')
            break
        else :
             print("invalid choice,please try again.")
   
    except  Exception as e :
        print(f"error :{e}")





