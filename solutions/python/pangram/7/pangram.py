"""Functions to determine if a sentence is a pangram."""


def is_pangram(sentence: str) -> bool:
    """Return whether a sentence is a pangram.

    Args:
        sentence (str): Sentence to check.

    Returns:
        bool: True if the sentence contains all 26 letters, False otherwise.
    """
    return set("abcdefghijklmnopqrstuvwxyz") <= set(sentence.lower())