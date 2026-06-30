"""Functions for computing the steps in the Collatz conjecture."""


def steps(number):
    """Return the number of steps required to reach 1 using the Collatz rules.

    Args:
        number (int): A positive integer.

    Returns:
        int: The number of steps to reach 1.

    Raises:
        ValueError: If number is not a positive integer.
    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    step = 0
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1
        step += 1
    return step
