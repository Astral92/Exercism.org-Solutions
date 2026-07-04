def classify(number):
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    factors = []
    for divisor in range(1, number):
        if number % divisor == 0:
            factors.append(divisor)

    factors_sum = sum(factors)

    if factors_sum < number:
        return "deficient"

    if factors_sum > number:
        return "abundant"

    return "perfect"
