"""Functions to calculate Hamming distance."""


def distance(strand_a, strand_b):
    """Return the Hamming distance between two equal-length strands.

    Raises:
        ValueError: If the strands are not the same length.
        """
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    return sum(ltr_a != ltr_b for ltr_a, ltr_b in zip(strand_a, strand_b))