"""Functions that implement rotational cipher."""


def rotate(text: str, key: int) -> str:
    """Return text rotated by Caesar cipher.

    Args:
        text (str): Text to rotate.
        key (int): Number of positions to shift letters by.

    Returns:
        str: The rotated text. Non-letter characters are unchanged."""
    key %= 26
    out = []

    for char in text:
        if "a" <= char <= "z":
            out.append(chr((ord(char) - ord("a") + key) % 26 + ord("a")))

        elif "A" <= char <= "Z":
            out.append(chr((ord(char) - ord("A") + key) % 26 + ord("A")))

        else:
            out.append(char)
    return "".join(out)