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
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            divisor_sum += divisor
            quotient = number // divisor
            if quotient != divisor:
                divisor_sum += quotient
        divisor += 1

    if divisor_sum < number:
        return "deficient"
    if divisor_sum > number:
        return "abundant"
    return "perfect"