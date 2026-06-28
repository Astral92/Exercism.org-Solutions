"""Functions to calculate the number and total of grains of wheat on a chessboard."""


def square(number):
    """Return the number of grains on the given chessboard square.

    Args:
        number (int): The square number.

    Returns:
        int: The number of grains on that square.
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    """Return the total number of grains on the chessboard."""
    return 2 ** 64 - 1
