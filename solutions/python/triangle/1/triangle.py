def equilateral(sides):
    a ,b ,c = sides
    return a == b == c and sum(sides) != 0


def isosceles(sides):
    a ,b ,c = sides
    return ((a == b and sum(sides) >= 2 * c) or (a == c and sum(sides) >= 2 * b) or (b == c and sum(sides) >= 2 * a)) 


def scalene(sides):
    c, a ,b = sides
    two_sides_collection = [(a, b), (b, c), (a, c)]
    return (a != b and a != c and b != c) and all((sum(two_sides) >= side for two_sides, side in zip(two_sides_collection, sides)))
