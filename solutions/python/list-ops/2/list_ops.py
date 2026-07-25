def append(list1, list2):
    for item in list2:
        list1.append(item)
    return list1


def concat(lists):
    total = []
    for list in lists:
        for item in list:
            total.append(item)
    return total


def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    count = 0
    for _ in list:
        count += 1

    return count


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    for item in list:
        initial = function(initial, item)

    return initial


def foldr(function, list, initial):
    for item in list[::-1]:
        initial = function(initial, item)

    return initial


def reverse(list):
    def go(xs, acc):
        if xs == []:
            return acc

        return go(xs[1:], [xs[0]] + acc)

    return go(list, [])
