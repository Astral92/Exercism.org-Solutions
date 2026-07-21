"""Functions to flatten nested iterables into a single list."""

from collections.abc import Iterable


def flatten(iterable):
    """Flatten a nested iterable into a list (excluding str/bytes/bytearray) and ignores None values.

    Args:
        iterable: An iterable.

    Returns:
        list: A flattened list of elements."""
    result = []

    def walk(item):
        if item is None:
            return

        if isinstance(item, Iterable) and not isinstance(item, (str, bytes, bytearray)):
            for element in item:
                walk(element)

        else:
            result.append(item)

    walk(iterable)

    return result