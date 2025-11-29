# creating a dictionary
student = {
    'name': 'john',
    'age': 34,
    'course':'computer',
    'marks': [78,90,77,88]
}

#print(student['course'])  

#accessing dictionary elements
#print(student.get('ag','age not found'))

# removing from dict
#student.pop('age')
#total = sum(student['marks'])
#avg = total / 4
#print(total)
#print(avg)

for key in student:
    print(key, student[key])


