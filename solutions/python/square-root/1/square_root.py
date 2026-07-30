def square_root(number):
    low = 1
    high = number

    while True:
        mid = (low + high) // 2
        if mid * mid > number:
            high = mid - 1

        elif mid * mid < number:
            low = mid + 1

        else:
            break

    return mid
