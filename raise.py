while True:
    try:
        age =int(input("enter your age:"))
        if age < 0:
            print("age cannot be negative")
            continue
        elif age >= 18:
            print(f"your are {age} yrs old, You are qualified !")
            break
        else :
            print("you have not met the age requirement")
    except ValueError:
        print("invalid input,try again!")