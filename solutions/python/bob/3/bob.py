def response(hey_bob: str):
    white_space_characters = {"\n", "\t", "\r"}
    if hey_bob.strip().endswith("?") and not hey_bob.isupper():
        return "Sure."

    if hey_bob.isupper() and not hey_bob.endswith("?"):
        return "Whoa, chill out!"

    if hey_bob.upper().endswith("?"):
        return "Calm down, I know what I'm doing!"

    if not hey_bob.strip() or any(char in white_space_characters for char in hey_bob):
        return "Fine. Be that way!"

    
    return "Whatever."