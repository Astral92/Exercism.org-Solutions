def score(x, y):
    square_distance = x**2 + y**2

    if square_distance <= 1:
        return 10

    if square_distance <= 25:
        return 5

    if square_distance <= 100:
        return 1

    return 0
