# This pseudocode is intended to determine whether students have
# passed or failed a course; student needs to average 60 or
# more on two tests. 
def main():
    # Constants
    PASSING = 60
    
    # Step 1: Initialize the first test score (set to a non-zero value to start the loop)
    firstTest = -1  # Start with a value that ensures the loop will run

    # Step 2: Start the loop
    while firstTest != 0:  # Continue until the user enters 0 to quit
        # Get the first test score from the user
        firstTest = float(input("Enter first score or 0 to quit: "))
        
        # Exit if the user enters 0 for the first test score
        if firstTest == 0:
            break
        
        # Get the second test score from the user
        secondTest = float(input("Enter second score: "))
        
        # Step 3: Calculate the average
        average = (firstTest + secondTest) / 2
        
        # Step 4: Output the average score
        print(f"Average is {average}")
        
        # Step 5: Check if the student passed or failed
        if average >= PASSING:
            print("Pass")
        else:
            print("Fail")

# Run the main function
if __name__ == "__main__":
    main()
