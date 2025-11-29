number_str=input('enter  digits:')
reverse_digit= "" #stores the reversed digit
for i in number_str: # loop over the digits in the string
    reverse_digit=i + reverse_digit
print(reverse_digit)