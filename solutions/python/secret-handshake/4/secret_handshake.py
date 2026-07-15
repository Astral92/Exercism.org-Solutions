"""Functions to convert numbers into a secret handshake."""

def commands(binary_str: str) -> list[str]:
    """Return the secret handshake.
    
    Args:
        binary_str (str): A binary string; only the rightmost five bits are used..
    
    Returns:
        list: The Handshake actions in order.
    """
    
    binary_str = binary_str.zfill(5)
    actions = ["wink", "double blink", "close your eyes", "jump"]
    result = [action for bit, action in zip(binary_str[-4:][::-1], actions) if bit == "1"]

    
    return result[::-1] if binary_str[-5] == "1" else result