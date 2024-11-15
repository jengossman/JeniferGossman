# This pseudocode is intended to determine whether students have
# passed or faiiled a course; student needs to average 60 or
# more on two tests

def main():
    # Constant for passing score
    PASSING = 60  # Define the passing score here
    
    # Step 1: Input first test score
    firstTest = float(input("Enter first score or 0 to quit: "))

    # Step 2: Loop until firstTest is 0
    while firstTest != 0:
        # Step 3: Input second test score
        secondTest = float(input("Enter second score: "))
        
        # Step 4: Calculate the average of both scores
        average = (firstTest + secondTest) / 2
        print(f"Average is {average}")
        
        # Step 5: Check if the student passed or failed
        if average >= PASSING:
            print("Pass")
        else:
            print("Fail")
        
        # Step 6: Ask for the first score again or 0 to quit
        firstTest = float(input("Enter first score or 0 to quit: "))
    
    # End of job
    print("End of program")

# Run the main function
if __name__ == "__main__":
    main()