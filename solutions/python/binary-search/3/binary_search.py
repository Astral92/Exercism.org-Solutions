"""Binary search functions."""

def find(search_list, value):
    """Return the index of the value in search_list.
    
    Args:
        search_list (list[int]): Sorted list of numbers to search.
        value (int): Value to search for.
        
    Returns:
        int: The index of the matching value

    Raises:
        ValueError: if value is not in the list.
    """
    low = 0
    high = len(search_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if search_list[mid] < value:
            low = mid + 1
        elif search_list[mid] > value:
            high = mid - 1
        else:
            return mid

    raise ValueError("value not in array")