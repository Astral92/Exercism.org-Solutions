"""Functions to determine if a sentence is a pangram."""


def is_pangram(sentence: str):
    """Return whether a sentence is a pangram.

    Args:
        sentence (str): Sentence to check.

    Returns:
        bool: True if the sentence contains all 26 letters, False otherwise.
    """
    unique_letters = 0
    letters = "abcdefghijklmnopqrstuvwxyz"
    for letter in letters:
        if letter in sentence.lower():
            unique_letters += 1

    return unique_letters == 26