class employee: # the main class
    def __init__(self, name, salary):
        self.name= name
        self.salary= salary

class manager(employee): # inherits from the employee class
    def __init__(self, name, salary, team_size): # initializes
        super().__init__(name, salary)
        self.team_size=team_size

    def display(self):
        print(f"{self.name} gets a salary of {self.salary} and is incharge of a {self.team_size} team department")

class developer(employee): # inherits from the employee class
    def __init__(self, name, salary, programming_language): # initializes
        super().__init__(name, salary)
        self.programming_language= programming_language

    def display(self):
        print(f"{self.name} gets a salary of {self.salary} and is an expert of {self.programming_language}")
   # creates an instance of thee manager and developer classes 
manager1=manager('alicia mueni', 120000, '20 people')
developer1= developer('bob robert', 300000, 'python')
# call methods from both thee manager and developer classes
manager1.display() # displays the managers details
developer1.display() # displays the developers details



        