"""Functions to determine if a sentence is a pangram."""


def is_pangram(sentence: str):
    """Return whether a sentence is a pangarm.

    Args:
        sentence (str): Sentence to check.

    Returns:
        bool: True if the count of unique alphabet letters is 26, false otherwise.
    """
    unique_letters = 0
    letters = "abcdefghijklmnopqrstuvwxyz"
    for letter in set(sentence.lower()):
        if letter in letters:
            unique_letters += 1

    return unique_letters == 26