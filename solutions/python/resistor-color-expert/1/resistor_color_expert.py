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

tolerance = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10,
}


def resistor_label(colors):

    if colors == ["black"]:
        return "0 ohms"

    r = (
        int("".join((str(color_codes[c]) for c in colors[:-2])))
        * 10 ** color_codes[colors[-2]]
    )

    for threshold, prefix in ((10**6, "mega"), (10**3, "kilo")):
        if r >= threshold:
            value = r / threshold
            if value.is_integer():
                value = int(value)
            return f"{value} {prefix}ohms ±{tolerance[colors[-1]]}%"

    return f"{r} ohms ±{tolerance[colors[-1]]}%"