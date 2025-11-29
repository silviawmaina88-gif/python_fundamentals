

## 🐍 Python Program: Average Calculator


# Initialize a variable to store the total sum
total_sum = 0

# Set the number of inputs we expect
NUM_COUNT = 5

# Loop to prompt the user for five numbers
for i in range(NUM_COUNT):
    while True:
        try:
            # Get input from the user, converting it to a floating-point number
            user_input = float(input(f"Enter number {i + 1} of {NUM_COUNT}: "))
            total_sum += user_input
            break  # Exit the inner loop if input is valid
        except ValueError:
            # Handle cases where the user enters non-numeric text
            print("That wasn't a valid number. Please try again.")

# Calculate the average
average = total_sum / NUM_COUNT

# Print the final result, formatted to two decimal places
print(f"\nThe sum of the numbers is: {total_sum}")
print(f"The average of the {NUM_COUNT} numbers is: {average:.2f}")



|

