"""Basic list operations implementation without using existing functions"""


def append(list1, list2):
    """Add all items from list2 to the end of list1 then return list1."""
    for item in list2:
        list1.append(item)
    return list1


def concat(lists):
    """Return a flattened list containing all items from each list in lists."""
    return [item for list in lists for item in list]


def filter(function, list):
    """Return the items in list for which function(item) is true."""
    return [item for item in list if function(item)]


def length(list):
    """Return the number of items in the list"""
    count = 0
    for _ in list:
        count += 1

    return count


def map(function, list):
    """Return a list of function(item) for each item in list."""
    return [function(item) for item in list]


def foldl(function, list, initial):
    """Fold items in list from the left into initial using function."""
    for item in list:
        initial = function(initial, item)

    return initial


def foldr(function, list, initial):
    """Fold items in list from the right into initial using function."""
    for item in list[::-1]:
        initial = function(initial, item)

    return initial


def reverse(list):
    """Return a new list with the items of list in reversed order."""
    result = []
    for item in list:
        result = [item] + result

    return result
        
