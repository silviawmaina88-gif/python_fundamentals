# implementing multiple inheritance in python
class A:
    def _init_(self):
        print("Here is class A")
class B:
    def _init_(self):
        print("Here is class B")
    
    def register(self):
        print("You are registered")

class C(B,A): # multiple inheritance
    def _init_(self):
        super()._init_()
        print("here is class C")

c=C() # object creation