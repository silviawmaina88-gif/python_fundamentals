#student grade management system
def save_student_record(filename, student_id, name, grade):
    """save a student record to a string"""
    with open(filename, 'a') as file:
        file.write(f"{student_id}, {name}, {grade} \n")
        print(f"record saved for {name}")

def read_all_students(filename):
    """read and display all students records"""
    try:
        with open(filename, 'r') as file :
            print("\n---students records ---")
            print(f"{'ID':<10} {'Name' : <20} {'grade':<5}")
            print("-" * 35)
            for line in file:
                student_id, name , grade, = line.strip().split(',')
                print(f"{student_id:<10} {name :<20} {grade:<5}")
    except FileNotFoundError:
        print("no records found. file does not exist.")

def search_student(filename,search_id):
    """search for a student by id"""
    try:
        with open(filename, 'r') as file:
            for line in file:
                student_id, name, grade =line.strip().split(',')
                if student_id == search_id:
                    print(f"found : {name}, grade : {grade}")
                    return
                
            print(f"student with id {search_id} not found")
                    
    except FileNotFoundError:
        print("no records found. file does not exist.")

# example usage
filename = 'students.txt'
# save some records
#save_student_record(filename, "101", "alice johnson", "A")
#save_student_record(filename, "102", "bob smith", "B")
save_student_record(filename, "103", "charlie brown", "A")

# read all records
read_all_students(filename)
# search for a specific student
search_student(filename,"103")
