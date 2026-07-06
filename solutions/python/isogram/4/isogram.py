"""Functions to determine whether a phrase is an isogram."""

def is_isogram(phrase: str) -> bool:
    """Return True if the phrase is an isogram.

    Args:
        phrase: String to check.

    Returns:
        True if the phrase is an isogram, otherwise False.
    """
    seen = set()
    for char in phrase:
        if char.isalpha():
            lower = char.lower()
            if lower in seen:
                return False
            seen.add(lower)
    return True
