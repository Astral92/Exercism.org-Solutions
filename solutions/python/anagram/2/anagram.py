"""Functions to find anagrams of a word."""

def find_anagrams(word, candidates):
    """Return anagrams of the target word.

    Args:
        word (str): The target word.
        candidates (list[str]): Candidate words to check.

    Returns:
        list: Anagrams from the candidate list.
                
    """
    word_lower = word.lower()
    matches = []
    
    for candidate in candidates:
        candidate_lower = candidate.lower()
        if sorted(word_lower) == sorted(candidate_lower) and word_lower != candidate_lower:
            matches.append(candidate)
            
    return matches
