total=0
number=-1 #start with a negative number so that the loop runs once
while number != 0:
    number=int(input("enter a number:"))
    total=total+ number # add the entered number to the total
    print(f"the total sum of the numbers you entered is:{total}")
