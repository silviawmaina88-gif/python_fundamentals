history = []
def calculator():
    """a menu-driven calculator with operation history ."""

    def get_numbers():
        """safely get two numbers from the user."""
        while True :
            try:
                a=float(input("enter firrst number:"))
                b=float(input("enter second number:"))
                return a, b
            except ValueError:
                print("invalid input. please enter numbers only.")
    
    def add():
        a,b =get_numbers()
        result = a+b
        history.append(f"added : {a} + {b} = {result}")
        print(f"result: {a} + {b} = {result}")

    def subtract():
        a,b =get_numbers()
        result = a-b
        history.append(f"subtracted :{a} - {b} = {result}")
        print(f"result: {a} - {b} = {result}")
    
    def multiply():
        a,b =get_numbers()
        result = a * b
        history.append (f"multiplied : {a} *{b} = {result}")
        print(f"result: {a} * {b} = {result}")

    def divide():
        a,b = get_numbers()
        if b == 0:
            print("error: division by zero i not allowed !")
            result= a/b
            history.append (f"divided : {a} / {b} = {result}")
            print(f"result : {a} / {b} = {result}")

    def show_histroy ():
        if not history :
            print("no history yet.")
        else :
            print("\n === calculation history ===")
            for i , entry in enumerate (history,1):
                print(f"{i}. {entry}")

    def clear_history():
        history.clear()
        print("history cleared !")

    def show_menu():
        print("\n" + "=" * 40)
        print("simple calculator")
        print("=" * 40)
        print("1. addition")
        print("2.subtraction")
        print("3. multiplication")
        print("4. division")
        print("5. show history")
        print("6. clear histrory")
        print("7.exit")
        print("=" * 40)

        # main programme loop
        while True :
            show_menu()
            choice = input ("enter choice (1-7):").strip()

            if choice == "1" :
                add()
            elif choice == "2":
                subtract()
            elif choice =="3":
                multiply()
            elif choice =="4":
                divide()
            elif choice == "5":
                show_histroy()
            elif choice == "6":
                clear_history()
            elif choice == "7":
                print ("thank you for using the calculator . goodbye !")
                break
            else :
                print ("invalid choice ! please enter a number between 1 and 7.")


calculator()
