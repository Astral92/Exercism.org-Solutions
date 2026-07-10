"""Functions that implement rotational cipher."""


def rotate(text: str, key: int) -> str:
    """Return shifted text using a rotational cipher.

    Args:
        text (str): Text to shift.
        key (int): Amount to shift by.

    Returns:
        str: Shifted text."""
    key %= 26
    out = []

    for ch in text:
        if "a" <= ch <= "z":
            out.append(chr((ord(ch) - ord("a") + key) % 26 + ord("a")))

        elif "A" <= ch <= "Z":
            out.append(chr((ord(ch) - ord("A") + key) % 26 + ord("A")))

        else:
            out.append(ch)
    return "".join(out)
