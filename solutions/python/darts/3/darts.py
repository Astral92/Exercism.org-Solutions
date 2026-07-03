"""Functions for calculating dart scores."""


def score(x, y):
    """Return the score for dart landing at coordinates (x,y).

    The target is centered at (0,0) with cocentric circles at radii 1, 5 , and 10.

    Args:
        x (float): Horizontal coordinate.
        y (float): Vertical coordinate.

    Returns:
        int: The score earned (0, 1, 5, or 10 points).
    """
    distance_squared = x**2 + y**2

    if distance_squared <= 1:
        return 10
    if distance_squared <= 25:
        return 5
    if distance_squared <= 100:
        return 1
    return 0
