# demonstarting inheritance

class Person: #parent class 
    def _init_(self, name, age): # constructor
        self.name = name
        self.age = age

    def greet(self): 
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

class Student(Person): # child class
    def _init_(self, name, age, student_id): # initialization constructor
        super()._init_(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying and has an id {self.student_id}")

# Create an instance of the Student class
student1 = Student("Alice", 20, "S12345")

# Call methods from both the Person and Student classes
student1.greet()  # Inherited from Person
student1.study()  # Defined in Student