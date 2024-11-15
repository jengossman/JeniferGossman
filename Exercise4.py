# This pseudocode segment is intended to compute and display
# the cost of home ownership for any number of users
# The program ends when a user enter 0 foro the mortgage payment

def startUp():
    """Prompt user for mortgage payment or 0 to quit."""
    mortgagePayment = float(input("Enter your mortgage payment or 0 to quit: "))
    return mortgagePayment

def mainLoop(mortgagePayment):
    """Prompt user for utilities, taxes, and upkeep, then calculate total."""
    utilities = float(input("Enter utilities: "))
    taxes = float(input("Enter taxes: "))
    upkeep = float(input("Enter amount for upkeep: "))
    
    # Calculate total cost
    total = mortgagePayment + utilities + taxes + upkeep
    print(f"Total is {total}")
    
def finishUp():
    """Display the end of the program message."""
    print("End of program")

def main():
    """Main function to control the program flow."""
    mortgagePayment = startUp()
    
    while mortgagePayment != 0:
        mainLoop(mortgagePayment)
        mortgagePayment = startUp()  # Ask for the mortgage payment again

    finishUp()

# Run the main function
if __name__ == "__main__":
    main()
