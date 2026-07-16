"""Functions to find anagrams of a word."""

from collections import Counter


def find_anagrams(word, candidates):
    """Return anagrams of the target word.

    Args:
        word (str): The target word.
        candidates (list[str]): Candidate words to check.

    Returns:
        list: Anagrams from the candidate list.

    """

    word_lower = word.lower()
    word_count = Counter(word_lower)
    matches = []

    for candidate in candidates:
        candidate_lower = candidate.lower()
        if word_count == Counter(candidate_lower) and word_lower != candidate_lower:
            matches.append(candidate)

    return matches