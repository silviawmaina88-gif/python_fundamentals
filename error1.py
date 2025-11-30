def safe_file_read(filename):
    """read file with comprehensive error handling"""

    try:
        with open(filename, 'r') as file:
            content=file.read()
            return content
    except FileNotFoundError:
        print(f"error: the file {filename} does not exist")
        return None
    except PermissionError:
        print(f"error: permission denied to read '{filename}'.")
        return None
    except Exception as e :
        print(f"unexpected error : {e}")
        return None
    
    # test the function
content = safe_file_read('data.txt')
if content:
    print(content)