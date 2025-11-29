shopping_list = ['Milk', 'Bread','Juice','Butter','Choco']
# list are index based
# Milk = index 0
# Bread  = index 1
# Juice = index 2
shopping_item = shopping_list[3]
# print(shopping_item)

# slicing items in a list
sliced_items = shopping_list[1:] # prints from item at index 1 to the end
sliced_items = shopping_list[1:4] # prints from item at index 1 item at index 3
sliced_items = shopping_list[-1] # prints the last item in the list
#print(sliced_items)

# modifying list / changing the values in a list
shopping_list[0] = 'Ngano'
# print(shopping_list)

# appending item in a list
marks = [87,90,74,90,78,98]
new_marks = marks.append(88) # adds item at the end of the list
# print(marks)

# removing item in a list
numbers = [1,5,7,9,5,3,5,8]
# numbers.remove(9) # removes 1 from the list
numbers.pop(5) # removes item from a list by index
del numbers[2] # deletes item at given index
numbers.clear() # removes all items in a list
 print(numbers)


# looping thro a list
#numbers2 = [1,5,7,9,5,3,5,8]
#for number in numbers2:
   # if number == 9:
    #    break
    # print(number)


# task Eliminating duplicates in a list
numbers3 = [1,2,5,6,7,5,6,4,4,5,7,9,5,3,5,8]
unique_numbers = [] # will contain unique numbers
for number in numbers3: # looping the numbers
    if number not in unique_numbers: 
        unique_numbers.append(number)
#print(unique_numbers)