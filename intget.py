#input validation with exception handling
def get_integer_input(prompt):
    """get valid integer input from user"""
    while True:
        try:
            value=int(input(prompt))
            return value
        except ValueError:
            print("invalid input ! please enter a whole number")

# usage
age=get_integer_input("enter your age:")
print(f"your age is {age}")