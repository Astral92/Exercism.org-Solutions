def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    total = 0
    for ltr_a, ltr_b in zip(strand_a,strand_b):
        if ltr_a != ltr_b:
            total += 1
    return total