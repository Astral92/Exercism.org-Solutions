def translate(text: str):

    VOWELS = ("a", "e", "o", "i", "u")

    def start_consonant(txt: str):
        if not txt.startswith(VOWELS):
            if txt.startswith("y"):
                return "y"
            return txt[0] + start_consonant(txt[1:])

        else:
            return ""

 
    out = []
    for word in text.split():
        start_consonants = start_consonant(word)
        if word.startswith((*VOWELS, "xr", "yt")):
            out.append(word + "ay")

        elif word.startswith(start_consonants[:-1] + "qu"):
            out.append(
                word[len(start_consonants) + 1 :]
                + word[: len(start_consonants) + 1]
                + "ay"
            )

        elif word.startswith(start_consonants[:-1] + "y") and not word.startswith("y"):
            out.append(
                word[len(start_consonants) - 1 :]
                + word[: len(start_consonants) - 1]
                + "ay"
            )

        elif word.startswith(start_consonants):
            out.append(
                word[len(start_consonants) :] + word[: len(start_consonants)] + "ay"
            )

      
    return " ".join(out)