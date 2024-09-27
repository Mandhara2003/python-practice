def is_prime_or_even_odd(n):
    # Check if the input is within the specified range
    if n < 1 or n > 1000:
        return "Input must be an integer between 1 and 1000."

    # Function to check if a number is prime
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Check if n is prime
    if is_prime(n):
        return True
    else:
        # Return "Even" or "Odd"
        if n % 2 == 0:
            return "Even"
        else:
            return "Odd"

# Example usage
print(is_prime_or_even_odd(11))  # Output: True (11 is prime)
print(is_prime_or_even_odd(8))   # Output: Even (8 is not prime and is even)
print(is_prime_or_even_odd(7))   # Output: True (7 is prime)
print(is_prime_or_even_odd(15))  # Output: Odd (15 is not prime and is odd)
print(is_prime_or_even_odd(1001))  # Output: Input must be an integer between 1 and 1000.