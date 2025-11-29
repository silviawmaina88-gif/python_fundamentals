# writing text to a file 
#with open("student_data.txt", 'w') as  file:
    #file.write("student name : Alice Johnson \n")
    #file.write("student ID : 12345 \n") #\n adds a new line after each line
    #file.write("grade : A \n")
    #print("data written succesfully")
with open("student_data.txt", 'a') as  file: # use 'a' if you want to read the existing data
    file.write("student name : Alice Johnson \n")
    file.write("student ID : 12345 \n") #\n adds a new line after each line
    file.write("grade : A \n")
    print("data written succesfully")

    # the file is automaticaly closed with the with block
# reading from a file
    #read entire file as a single string
    #with open("student_data.txt" , 'r' ) as file :
            #content = file.read()
            #print(content)
    # read line by line
    #with open("student_data.txt" , 'r') as file :
          #for line in file:
                #print(line.strip()) # strip() removes trailing new line

          
    # read all lines into a list
    #with open("student_data.txt" , 'r') as file :
        #lines= file.readlines()
        #print(f"total lines : {len(lines)}")
        #for line in lines:
            #print(line.strip())

# append new student data
    with open("student_data.txt" , 'a') as file :
        file.write("\n student name\     : Bob smith \n")
        file.write("student ID : 12346 \n")
        file.write("grade : B \n")

    print("data appended successfully")

    # read and display updated file
    with open("student_data.txt" , 'r') as file:
        print(file.read())

