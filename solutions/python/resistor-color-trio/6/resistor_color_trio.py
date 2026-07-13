"""Functions to calculate resistance."""

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

def label(colors: list[str]) -> str:
    """Return the resistance value.
    
    Args:
        colors (list[str]): List of resistor colors.
        
    Returns:
        str: Resistance value as a formated string.
    """
    resistance = (10 * color_codes[colors[0]] + color_codes[colors[1]]) * 10 ** color_codes[colors[2]]

    if resistance != 0:
        if resistance % 10**9 == 0:
            return f"{resistance // 10**9} gigaohms"
        if resistance % 10**6 == 0:
            return f"{resistance // 10**6} megaohms"
        if resistance % 10**3 == 0:
            return f"{resistance // 10**3} kiloohms"

    return f"{resistance} ohms"