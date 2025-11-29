def average(number_list):
    """takes list of numbers and returns their average"""
    if not number_list:
        return 0
    total=sum(number_list)
    count = len (number_list)
    return total/count

data= [10,90,80,60,45,]
avg=average(data)
print(f"the list is:{data}")
print(f"the average of numbers is:{avg}")