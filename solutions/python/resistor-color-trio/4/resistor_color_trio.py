"""Functions to calculate the resistance."""

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
    """Return the resistence value.
    
    Args:
        colors (list): List of colors.
        
    Returns:
        (str): Resistance value.
    """
    resistance = (10 * color_codes[colors[0]] + color_codes[colors[1]]) * 10 ** color_codes[colors[2]]

    if resistance != 0:
        if resistance % 10**9 == 0:
            return f"{resistance // 10**9} gigaohms"
        elif resistance % 10**6 == 0:
            return f"{resistance // 10**6} megaohms"
        elif resistance % 10**3 == 0:
            return f"{resistance // 10**3} kiloohms"

    return f"{resistance} ohms"