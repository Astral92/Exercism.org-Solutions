
def square(number):
    if not 64 >= number >= 1:
        raise ValueError("square must be between 1 and 64")
    if number == 1:
        return 1
    return 2 * square(number - 1)



def total():
     return sum([square(number) for number in range(1,65)])
