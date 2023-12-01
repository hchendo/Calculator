def add(numbers):
    """
    Returns the sum of a and b.
    """
    return numbers[0] + numbers[1]

def subtract(numbers):
    """
    Returns the difference of a and b.
    """
    return numbers[0] - numbers[1]

def multiply(numbers):
    """
    Returns the product of a and b.
    """
    return numbers[0] * numbers[1]

def divide(numbers):
    """
    Returns the division of a by b.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return numbers[0] / numbers[1]
