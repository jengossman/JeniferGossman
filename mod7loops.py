# Create a list of 15 numbers
numbers = [12, 7, 34, 45, 23, 8, 56, 67, 89, 101, 44, 33, 22, 10, 5]

# Loop through the list of numbers
for number in numbers:
    # Check if the number is even or odd
    if number % 2 == 0:
        print(str(number) + " is even")  # Convert number to string and print
    else:
        print(str(number) + " is odd")  # Convert number to string and print
