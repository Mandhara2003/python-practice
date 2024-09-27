def multiplication_table(number):
    # Check if the input is an integer
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    
    # Check if the number is within the specified range
    if number < 1 or number > 20:
        raise ValueError("Input must be between 1 and 20 inclusive.")
    
    # Print the multiplication table
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Example usage
multiplication_table(5)

# Example error cases
# multiplication_table(0)    # Raises ValueError
# multiplication_table(21)   # Raises ValueError
# multiplication_table(10.5) # Raises TypeError