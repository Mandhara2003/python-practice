def categorize_temperature(temp):
    # Check if the input is a float
    if not isinstance(temp, (float, int)):
        raise TypeError("Temperature must be a number.")
    
    # Check if the temperature is within the specified range
    if temp < -50.0 or temp > 50.0:
        raise ValueError("Temperature must be between -50.0 and 50.0.")

    # Determine the temperature category
    if temp > 30:
        return "Hot"
    elif 20 <= temp <= 30:
        return "Warm"
    elif 10 <= temp <= 19:
        return "Cool"
    else:
        return "Cold"

# Example usage
print(categorize_temperature(35.0))  # Output: Hot
print(categorize_temperature(25.5))  # Output: Warm
print(categorize_temperature(15.0))  # Output: Cool
print(categorize_temperature(5.0))   # Output: Cold

# Example error cases
# print(categorize_temperature(60.0))  # Raises ValueError
# print(categorize_temperature(-60.0))  # Raises ValueError
# print(categorize_temperature("25"))   # Raises TypeError