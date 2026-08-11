import re


def translate(text: str):

    out = []
    for word in text.split():
        match = re.match(
            r"[aeiou]|xr|yt|[b-df-hj-np-tv-z]*qu|[b-df-hj-np-tv-z]+y|[b-df-hj-np-tv-z]+",
            word,
        )
        if match:
            prefix = match.group()
            if prefix in ("a", "e", "i", "o", "u", "xr", "yt"):
                out.append(word + "ay")

            elif prefix.endswith("y") and len(prefix) != 1:
                out.append(word[match.end() - 1 :] + prefix[:-1] + "ay")

            else:
                out.append(word[match.end() :] + prefix + "ay")

    return " ".join(out)