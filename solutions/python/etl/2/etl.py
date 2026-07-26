"""Change data format from one-to-many (score -> letters) to one-to-one mapping (letter -> score."""

def transform(legacy_data):
    """Convert score -> [letters] into letter -> score (letters are lowercased).
    
    Args:
        legacy_data (dict): Mapping of integer scores to iterable collection of letters.
        
    Returns:
        dict: Mapping each lower-case letter to its integer score."""
    data = {}
    for key,letters in legacy_data.items():
        for letter in letters:
            data[letter.lower()] = key
    return data
