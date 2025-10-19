def gcd(a, b):
    """Calculates the GCD of a and b using the Euclidean Algorithm."""
    # The loop continues until the remainder (b) is 0
    while b:
        # Standard Python tuple assignment for simultaneous update:
        # a takes the old value of b, and b takes the remainder of a / b
        a, b = b, a % b
    return a

# --- Example Usage ---
num1 = 54   # Factors: 1, 2, 3, 6, 9, 18, 27, 54
num2 = 24   # Factors: 1, 2, 3, 4, 6, 8, 12, 24
result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}") # Output: 6
