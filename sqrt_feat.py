import math

def sqrt(number):
    """Returns the square root of a number."""
    if number < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    return math.sqrt(number)

# Example usage
if __name__ == "__main__":
    print(sqrt(9))  # Output should be 3.0
