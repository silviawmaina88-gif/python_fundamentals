def check_age():
    """checks if the person is a senior citizen,adult,teenager or a toddler"""
    try:
        age=int(input("enter your age:"))
        if age >=65:
            print(f"wow your{age},enjoy your retirement")
        elif age >=18:
            print(f"wewe ni raia at {age},be ready to vote and pay taxes")
        elif age >= 13:
            print(f"at {age},tulia bro uende high school utajua ujui")
        elif age >= 0 :
            print(f"OMG {age},enjoy a care free life while you still can")
        else:
            print("age cannot be negative,enter a valid number")
    except ValueError:
        print("invalid input,try again")

check_age()
