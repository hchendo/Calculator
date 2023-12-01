def add(numbers):
    """
    Returns the sum of numbers[0] and numbers[1].
    """
    return numbers[0] + numbers[1]

def subtract(numbers):
    """
    Returns the difference of numbers[0] and numbers[1].
    """
    return numbers[0] - numbers[1]

def multiply(numbers):
    """
    Returns the product of numbers[0] and numbers[1].
    """
    return numbers[0] * numbers[1]

def divide(numbers):
    """
    Returns the division of numbers[0] and numbers[1].
    """
    if numbers[1] == 0:
        raise ValueError("Cannot divide by zero.")
    return numbers[0] / numbers[1]
