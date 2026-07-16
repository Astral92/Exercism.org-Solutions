def find_anagrams(word, candidates):
    word_lower = word.lower()
    matches = []
    
    for candidate in candidates:
        candidate_lower = candidate.lower()
        if sorted(word_lower) == sorted(candidate_lower) and word_lower != candidate_lower:
            matches.append(candidate)
            
    return matches
