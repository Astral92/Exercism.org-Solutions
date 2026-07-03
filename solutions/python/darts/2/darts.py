"""Functions to calculate scores in a dart game."""

def score(x, y):
    """Return scores in a single dart game given a point in the target. 

    Args:
        x (float): Horizontal position.
        y (float): Vertical postion.

    Returns:
        int: Score earned by landed at that point"""
    sqrt_d = x**2 + y**2

    if sqrt_d <= 1:
        return 10

    if sqrt_d <= 25:
        return 5

    if sqrt_d <= 100:
        return 1

    return 0