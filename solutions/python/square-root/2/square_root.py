def square_root(number):
    initial = number // 2 + 1
    while True:  
        s = (initial + number // initial) // 2
        if s * s == number:
            break
        initial = s

    return s
