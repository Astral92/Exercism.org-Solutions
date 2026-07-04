"""Functions to classify numbers based on Nicomachus scheme."""


def classify(number: int) -> str:
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    if number == 1:
        return "deficient"
    divisor_sum = 1
    i = 2
    while i * i <= number:
        if number % i == 0:
            divisor_sum += i
            quotient = number // i
            if quotient != i and quotient != number:
                divisor_sum += quotient
        i += 1

    if divisor_sum < number:
        return "deficient"
    elif divisor_sum > number:
        return "abundant"
    return "perfect"