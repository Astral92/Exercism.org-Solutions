"""Functions for Raindrops, a slightly more complex Fizzbuzz challenge"""


def convert(number):
    """Return raindrop sounds for a number.

    Args:
        number (int): Number to be converted.

    Returns:
        str: 'Pling' if divisible by 3, 'Plang' if divisible by 5,
             'Plong' if divisible by 7, or any combination of these.
             Returns the number as a string if none apply.
    """
    result = ""
    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"

    return result or str(number)