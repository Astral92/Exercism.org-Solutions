"""Functions to calculate the number of grains of wheat on a chessboard."""


def square(number):
    if not 64 >= number >= 1:
        raise ValueError("square must be between 1 and 64")
    if number == 1:
        return 1
    return 2 * square(number - 1)


def total():
    return sum(square(number) for number in list(range(1, 65)))
