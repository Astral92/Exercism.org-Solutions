from string import ascii_lowercase


def rotate(text: str, key: int) -> str:
    rotated = ""
    for i in text:
        if i.isalpha():
            old = ascii_lowercase.index(i.lower())
            new = old + key
            if new > 25:
                new = new % 26
            if i.isupper():
                ltr = ascii_lowercase[new].upper()
            else:
                ltr = ascii_lowercase[new]
            rotated += ltr

        else:
            rotated += i

    return rotated

