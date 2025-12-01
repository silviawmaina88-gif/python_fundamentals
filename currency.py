# percentage formating
accuracy= 0.9567
print(f"model accuracy : {accuracy: .2%}") #formated as a percentage and rounded to two decimal places

#currency formating
prices=[19.99, 149.50, 5.00] # creates a list of prices
for price in prices:  #iterates over each value in the list
    print(f"price: ${price:>8.2f}") # 2f formats it as a float with two decimal places