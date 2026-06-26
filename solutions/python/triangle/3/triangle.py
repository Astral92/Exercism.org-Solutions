def equilateral(sides):
    side_a ,side_b ,side_c = sides
    return side_a == side_b == side_c and sum(sides) != 0


def isosceles(sides):
    side_a ,side_b ,side_c = sides
    return ((side_a == side_b and sum(sides) >= 2 * side_c) or (side_a == side_c and sum(sides) >= 2 * side_b) or (side_b == side_c and sum(sides) >= 2 * side_a)) 


def scalene(sides):
    side_c, side_a ,side_b = sides
    two_sides_collection = [(side_a, side_b), (side_b, side_c), (side_a, side_c)]
    return (side_a != side_b and side_a != side_c and side_b != side_c) and all((sum(two_sides) >= side for two_sides, side in zip(two_sides_collection, sides)))