numbers=[]
for i in range (5):
    while True:
        num=int(input(f"enter the numbers{i+1}:"))
        numbers.append(num)
        break
    print(numbers)
if numbers :
    largest= max(numbers)
    smallest=min(numbers)
    print(f"the largest number is:{largest}")
    print(f"the smallest number is:{smallest}")
    
