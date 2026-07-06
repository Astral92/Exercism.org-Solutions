"""Functions to determine if a word or phrase is an isogram/"""

def is_isogram(phrase: str) -> bool:
    seen = set()
    for ltr in phrase:
        if ltr.isalpha():
            lower = ltr.lower()
            if lower in seen:
                return False
            seen.add(lower)
    return True