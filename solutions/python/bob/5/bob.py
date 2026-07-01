"""Functions to determine what bob replies."""


def response(hey_bob: str):
    """Return bob's reply given what is said to him.

    Args:
        hey_bob (str): what is said to bob.

    Returns:
        str: bob's reply.
    """
    message = hey_bob.strip()
    is_yelling = message.isupper()
    is_question = message.endswith("?")
    is_silence = not message
    if is_silence:
        return "Fine. Be that way!"
    if is_question and not is_yelling:
        return "Sure."

    if is_yelling and not is_question:
        return "Whoa, chill out!"

    if is_yelling and is_question:
        return "Calm down, I know what I'm doing!"

    return "Whatever."
