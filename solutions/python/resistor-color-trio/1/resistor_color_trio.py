color_codes = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}


def label(colors: list[str]):
    code1 = color_codes[colors[0]]
    code2 = color_codes[colors[1]]
    zeros = 10 ** color_codes[colors[2]]
    r = (10 * code1 + code2) * zeros
    metric = " ohms"
    if r != 0:
        if r % 10**9 == 0:
            r = r // 10**9
            metric = " gigaohms"

        elif r % 10**6 == 0:
            r = r // 10**6
            metric = " megaohms"

        elif r % 10**3 == 0:
            r = r // 10**3
            metric = " kiloohms"

    return str(r) + metric

