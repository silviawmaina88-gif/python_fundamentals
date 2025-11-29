# creating a dictionary
# name_of_dictionary = {
#     'key':'value'
# }

student = {
    'name': 'John',
    'age': 22,
    'course': 'Computer Science'
}

# accessing dictionary elements using keys
# student_course = student['course']
# print(student_course)
# print(student['course'])

# accessing dictionary elements using get() method
# print(student.get('ag','age not found'))

#Adding and Updating Elements
shopping_list = {
    'milk':60,
    'bread':70,
    'sugar': 240
}
#print(shopping_list)
# adding an item in a dictionary
shopping_list['Nescafe'] = 10
# print(shopping_list)

# Removing Elements from a dictionary (pop method and del method)
# shopping_list.pop('bread')
del shopping_list['milk']
print(shopping_list)