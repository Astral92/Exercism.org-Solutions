"""Functions to determine validate an isbn."""


def is_valid(isbn: str):
    """Returns whether an isbn is valid.

    Args:
        isbn (str): The isbn.

    Returns:
        bool: True if it's a valid isbn, False otherwise.
    """

    processed_isbn = []
    isbn_sum = 0

    for index, char in enumerate(isbn):
        if char.isdigit():
            processed_isbn.append(int(char))

        elif char == "X" and index == len(isbn) - 1:
            processed_isbn.append(10)

        elif char.isalpha():
            return False

    if len(processed_isbn) != 10:
        return False
    processed_isbn.reverse()
    for number, digit in enumerate(processed_isbn, start=1):
        isbn_sum += number * digit
    return isbn_sum % 11 == 0