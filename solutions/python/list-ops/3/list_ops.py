"""Basic list operations implementation without using existing functions"""


def append(list1, list2):
    """Add all items in list2 to list1 then return list1."""
    for item in list2:
        list1.append(item)
    return list1


def concat(lists):
    """Return a flattened list with all items in all lists combined."""
    total = []
    for list in lists:
        for item in list:
            total.append(item)
    return total


def filter(function, list):
    """Apply function to every item in list then return a list with the results."""
    return [item for item in list if function(item)]


def length(list):
    """Calculate the length of a list."""
    count = 0
    for _ in list:
        count += 1

    return count


def map(function, list):
    """Return a list with the results of applying function(item) on all items in list. """
    return [function(item) for item in list]


def foldl(function, list, initial):
    """Fold each item in list on initial using function, from the left."""
    for item in list:
        initial = function(initial, item)

    return initial


def foldr(function, list, initial):
    """Fold each item in list on initial using function, from the right."""
    for item in list[::-1]:
        initial = function(initial, item)

    return initial


def reverse(list):
    """Return a list off all items in list in reversed order."""
    def go(xs, acc):
        if xs == []:
            return acc

        return go(xs[1:], [xs[0]] + acc)

    return go(list, [])
