"""Functions to determine whether a triangle is equilateral, isosceles or scalene."""

def is_triangle(sides):
    side_1, side_2 , side_3 = sides
    return side_1 > 0 and side_2 > 0 and side_3 > 0 and side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_2 + side_3 > side_1


def equilateral(sides):
    side_1, side_2 , side_3 = sides
    return is_triangle(sides) and side_1 == side_2 == side_3


def isosceles(sides):
    side_1, side_2 , side_3 = sides
    return is_triangle(sides) and (side_1 == side_2 or side_1 == side_3 or side_2 == side_3)


def scalene(sides):
    side_1, side_b , side_3 = sides 
    return is_triangle(sides) and (side_1 != side_b and side_1 != side_3 and side_b != side_3) 