"""Functions to determine whether a triangle is equilateral, isosceles or scalene."""


def is_triangle(sides):
    a, b, c = sides
    return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a


def equilateral(sides):
    a, b, c = sides
    return is_triangle(sides) and a == b == c


def isosceles(sides):
    a, b, c = sides
    return is_triangle(sides) and (a == b or a == c or b == c)


def scalene(sides):
    a, b, c = sides
    return is_triangle(sides) and (a != b and a != c and b != c)
