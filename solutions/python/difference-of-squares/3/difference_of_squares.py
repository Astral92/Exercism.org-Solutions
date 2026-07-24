"""Functions to calculate square of the sum, sum of the squares and the difference between them for the first N natural numbers."""


def square_of_sum(number):
    return (number * (number + 1) // 2) ** 2


def sum_of_squares(number):
    return number * (number + 1) * (2 * number + 1) // 6


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
