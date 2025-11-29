# classes in python
"""class is a blue print"""


# how to create a class
class Student:
    def _init_(self,name,age):
        self.name= name
        self.age=age
    
    # object creation
st1= Student("silvia",19)
    # accessing member of an object
student_name=st1.name
student_age = st1.age
print(f"your name is{student_name} and are {student_age}years old")
