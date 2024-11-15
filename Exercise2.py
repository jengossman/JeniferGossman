# This pseudocode is intended to display employee net pay values.
# All employees have a standard $45 deduction from their checks.
# If an employee does not earn enough to cover the deduction
# an error message is displayed.

def main():
    # Constants
    DEDUCTION = 45
    EOFNAME = "ZZZ"
    
    # Step 1: Input first name
    name = input(f"Enter first name or {EOFNAME} to quit: ")
    print(f"DEBUG: name = {name}")  # Debugging line
    
    # Step 2: Process until EOFNAME is entered
    while name != EOFNAME:
        # Step 3: Input hours worked and hourly rate
        hours = float(input(f"Enter hours worked for {name}: "))
        print(f"DEBUG: hours = {hours}")  # Debugging line
        
        rate = float(input(f"Enter hourly rate for {name}: "))
        print(f"DEBUG: rate = {rate}")  # Debugging line
        
        # Step 4: Calculate gross pay and net pay
        gross = hours * rate
        net = gross - DEDUCTION
        print(f"DEBUG: gross = {gross}, net = {net}")  # Debugging line
        
        # Step 5: Output net pay or handle deductions
        if net > 0:
            print(f"Net pay for {name} is {net}")
        else:
            print("Deductions not covered. Net is 0.")
        
        # Step 6: Prompt for next name or EOFNAME to quit
        name = input(f"Enter next name or {EOFNAME} to quit: ")
        print(f"DEBUG: next name = {name}")  # Debugging line

    # Step 7: End of job
    print("End of job")

# Run the main function
if __name__ == "__main__":
    main()

