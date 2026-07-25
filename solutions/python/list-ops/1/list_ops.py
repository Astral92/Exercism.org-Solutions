def append(list1, list2):

    return list1 + list2

def concat(lists):
    total = []
    for list in lists:
        total += list
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
    if list:
        for i in list:
            c = function(initial,i)
            initial = c

        return c

    return initial


def foldr(function, list, initial):
    if list:
        for i in list[::-1]:
            c = function(initial,i)
            initial = c

        return c

    return initial
    


def reverse(list):
    return list[::-1]
