# sales tax calculation
price=float(input('enter the price (ksh):'))
tax=float(input('enter the tax rate(%):'))
tax = tax* price # calculates the tax to be paid on the item
final_price= tax + price # calculate the basic price and the tax
print(final_price)



