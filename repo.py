# Example Python Codebase

# Inconsistent variable names
first_variable = 10
secondVariable = 20
Third_Variable = 30
FOURTH_VARIABLE = 40

# Function with inconsistent variable names
def calculate_sum(a, B, c):
    result = a + B + c
    return result

# Main function
def main():
    # Inconsistent variable names within function
    numberOne = 5
    NumberTwo = 10
    third_number = 15

    # Calling function with inconsistent variable names
    total = calculate_sum(numberOne, NumberTwo, third_number)
    print("Total sum:", total)

# Calling the main function
if __name__ == "__main__":
    main()