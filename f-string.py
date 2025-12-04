 # decimal precision
#pi= 3.14159265359
#price = 49.5
# control decimal places
#print(f"pi (2 decimals) : {pi : .2f}") # round off to 2  decimal
#print(f"pi (4 decimals) : {pi : .4f}") # round off to 4 decimals
#print(f"price : ${price : .2f}")

#  width abd alignment
#num = 142
#print(f"number : {num : 5}") # right-aligned in 5 spaces
#print(f"number : {num : <5}") # left-aligned
#print(f"number : {num : ^5}") # center-aligned
#print(f"number : {num : >5}") #right-aligned (explicit)

#padding with zeros
#print(f"ID : {num :05}")

     # formating tables
# student grade table
students=[
    ("alice johnson", 101, 95.5, "A"),
    ("bob smith", 102, 87.3, "B"),
    ("charlie brown", 103, 92.8, "A"),
    ("diana prince", 104, 78.5, "C")
]

# print header using f-string for formated output
# :<20 aligns the 'name' left in a 20-character space
# :<8 aligns 'ID','score' & 'grade' left in 8-character space
print(f"{'name': <20} {'ID': <8} {'score': <8} {'grade': <6}")
# print a separator line
print("-" * 42)
#iterate through the student data list

# print student data using f-string for formatted output
for name, student_id, score, grade in students:
    print(f"{name:<20} {student_id:<8} {score:<8.2f} {grade:<6} ")

