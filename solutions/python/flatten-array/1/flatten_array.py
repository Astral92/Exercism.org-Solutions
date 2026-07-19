from collections.abc import Iterable


def flatten(iterable):
    result = []

    def walk(x):
        if x is None:
            return
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes, bytearray)):
            for item in x:
                walk(item)
        else:
            result.append(x)

    walk(iterable)
    return result
