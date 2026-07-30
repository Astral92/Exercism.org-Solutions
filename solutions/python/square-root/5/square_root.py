"""Calculate the square root of a given number without using pre-existing modules or built-ins."""


def square_root(number):
    """Return the integer square root of the number if the number is a perfect square; return None otherwise."""
    low = 1
    high = number

    while low <= high:
        mid = (low + high) // 2
        square = mid * mid
        if square > number:
            high = mid - 1

        elif square < number:
            low = mid + 1

        else:
            return mid

    return None