import string


def parole_uniche (self, text: str) -> dict:

    parole_dict: dict = {}

    for token in text.split():

        parola = token.lower().strip(string.punctuation)

        if not token:
            continue

        parola = text.count(token)

        parole_dict[token] = parola 

    return parole_uniche