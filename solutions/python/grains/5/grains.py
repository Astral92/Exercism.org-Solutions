"""Functions to calculate the number and total of grains of wheat on a chessboard."""


def square(number):
    """Function to calculate the number of grains of wheat on a given chessboard square.

    Args:
        number (int): the square number.

    Returns:
        (int): the number of grains on that square
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

    return 2 ** (number - 1)


def total():
    return sum(square(number) for number in list(range(1, 65)))

