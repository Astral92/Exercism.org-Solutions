"""Functions to determine if a word or phrase is an isogram/"""

def is_isogram(phrase: str) -> bool:
    """Return whether a phrase or word is an isogram.
    
    Args:
        phrase (str): String to check.

    Returns:
        bool: True if the string is an isogram, False otherwise
    """
    seen = set()
    for ltr in phrase:
        if ltr.isalpha():
            lower = ltr.lower()
            if lower in seen:
                return False
            seen.add(lower)
    return True