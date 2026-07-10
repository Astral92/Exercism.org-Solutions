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

    for char in text:
        if "a" <= char <= "z":
            out.append(chr((ord(char) - ord("a") + key) % 26 + ord("a")))

        elif "A" <= char <= "Z":
            out.append(chr((ord(char) - ord("A") + key) % 26 + ord("A")))

        else:
            out.append(char)
    return "".join(out)
