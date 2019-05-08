import re

from shadok.language import Symbol
from shadok.path_to_success import ImproperShadokSyntax


class MagicFaucet:

    # Pourquoi faire simple quand on peut faire compilé ?
    PROPER_SHADOK_WORD = re.compile(
        r"(?P<word>([Gg][Aa]|[Bb][Uu]|[Zz][Oo]|[Mm][Ee][Uu]|[{digit}]+[\.,]?[{digit}]*)+)".format(
            digit="".join([l.value for l in Symbol if l.is_digit()])
        )
    )
    PROPER_NORMALIZED_SHADOK_WORD = re.compile(
        r"(?P<word>({letter}|[{digit}]+[\.,]?[{digit}]*)+)".format(
            letter="|".join([l.value for l in Symbol if l.is_letter()]),
            digit="".join([l.value for l in Symbol if l.is_digit()]),
        )
    )

    @staticmethod
    def normalize(text):
        text = text.lower()
        for symbol in Symbol:
            if symbol.is_letter():
                text = text.replace(symbol.name.lower(), symbol.value)
        # print("Normalized text: '%s'" % text)
        return text.split(" ")

    @staticmethod
    def check_syntax(text):
        if not isinstance(text, str):
            raise ValueError(
                "MagicFaucet.check_syntax(test:str) can only handle string not %s."
                % text.__class__.__name__
            )
        for word in text.split(" "):
            if word:
                result = re.finditer(MagicFaucet.PROPER_SHADOK_WORD, word)
                # print("REGEX MATCH %s for '%s' : %s" % (MagicFaucet.PROPER_SHADOK_WORD, word, result))
                matches = list(result)
                if len(matches) != 1 or matches[0].group() != word:
                    raise ImproperShadokSyntax(word, matches)

    @staticmethod
    def pretty_print(text):
        result = ""
        normalized_text = MagicFaucet.normalize(text)
        pretty_shadok = {
            Symbol.GA.value: "Ga",
            Symbol.BU.value: "Bu",
            Symbol.ZO.value: "Zo",
            Symbol.MEU.value: "Meu",
        }
        for character in " ".join(normalized_text):
            result += pretty_shadok.get(character, character)
        return result
