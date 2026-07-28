"""Calculate the sum of unique multiples of given base values below a certain limit."""


def sum_of_multiples(limit, bases):
    """Return the sum of all the unique numbers that are multiples of any base.

    For each base in `bases`, we generate base * k for k >= 1 such that base * k < limit. We then combine all generated numbers (dedpulicating them), and return their sum.

     Args:
        limit (int): Upper bound; only multiples strictly less than this are used.
        bases (list[int]): Unique, sorted base values (non-negative ints).

     Returns:
         int: Sum of unique generated multiples below `limit`."""

    unique = set()
    for base in bases:
        if base == 0:
            continue
        max_k = (limit - 1) // base
        for k in range(1, max_k + 1):
            unique.add(base * k)
    return sum(unique)
