def safe_divide(a, b):
    """safely divide two numbers with error handling"""
    try:
        result= a/b
        return result
    except ZeroDivisionError:
        print("error:cannot divide by zero")
        return None
    except TypeError:
        print("error: both agurments must be numbers")
        return None
    
#test the function
print(safe_divide(10,2)) # 5.0
print(safe_divide(10, 0)) #error:cannot divide by zero
print(safe_divide(10,'2')) #error:both agurments must be numbers
