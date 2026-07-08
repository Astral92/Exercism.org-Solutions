"""Functions to validate an isbn."""


def is_valid(isbn: str) -> bool:
    """Returns whether an isbn is valid.

    Args:
        isbn (str): The isbn.

    Returns:
        bool: True if it's a valid isbn, False otherwise.
    """
    cleaned = isbn.replace("-", "")

    if len(cleaned) != 10:
        return False
    
    total = 0
    
    for index, char in enumerate(cleaned):
        if char.isdigit():
            value = int(char)

        elif char == "X" and index == 9:
            value = 10

        else:
            return False

        total += (10 - index) * value
    
    return total % 11 == 0
