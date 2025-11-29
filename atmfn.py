#defining an atm withrawal function
accountBalance = 45000
def atmWithdrawal():
    amount = int(input("enter atmWithdrawal: "))
    if amount > accountBalance:
        print('insufficient balance')
    else:
       balance = accountBalance - amount
       print(f"your balance is {balance}")

atmWithdrawal()