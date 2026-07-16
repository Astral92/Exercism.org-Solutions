"""Functions to convert numbers into a secret handshake."""

CMDS = ("wink", "double blink", "close your eyes", "jump")


def commands(binary_str):
    """Return the secret handshake.

    Args:
        binary_str (str): A binary string; only the rightmost five bits are used..

    Returns:
        list: The Handshake actions in order.
    """
    number = int(binary_str, 2)
    result = [action for index, action in enumerate(CMDS) if number & 1 << index]

    return result[::-1] if number & 1 << 4 else result