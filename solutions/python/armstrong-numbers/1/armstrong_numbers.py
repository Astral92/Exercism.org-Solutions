"""Function to determine whether a number is an Armstrong number."""


def is_armstrong_number(number):
    """Return whether a number is an Armstrong number.

    Args:
        number (int): The number to inspect.

    Returns:
        bool: True if the number is an Armstrong number, False otherwise.
    """
    digits = str(number)
    number_of_digits = len(digits)
    return sum(int(digit) ** number_of_digits for digit in digits) == number
