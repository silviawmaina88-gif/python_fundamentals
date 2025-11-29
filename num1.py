n=int(input("enter a number:"))
total_sum=0
for number in range(1,n+1):
    total_sum=total_sum + number # add current number to the total
    print(f"the sum of numbers from i to n is :{total_sum}")