def is_isogram(phrase: str) -> bool:
    seen = set()
    for ltr in phrase:
        if ltr.isalpha():
            ltr = ltr.lower()
            if ltr in seen:
                return False
            seen.add(ltr)
    return True