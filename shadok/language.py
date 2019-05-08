import enum


class Symbol(enum.Enum):
    GA_DIGIT = "𝙾"
    BU_DIGIT = "−"
    ZO_DIGIT = "ᒧ"
    MEU_DIGIT = "◿"
    GA = "9"
    BU = "8"
    ZO = "7"
    MEU = "6"

    def is_digit(self):
        return self in [
            Symbol.GA_DIGIT,
            Symbol.BU_DIGIT,
            Symbol.ZO_DIGIT,
            Symbol.MEU_DIGIT,
        ]

    def is_letter(self):
        return self in [Symbol.GA, Symbol.BU, Symbol.ZO, Symbol.MEU]


# Careful the key must be formatted properly.
FRENCH_TRANSLATION = {
    "Ga": ["Moi", "Non", "Intérieur"],
    "GaBu": ["Notion"],
    "GaGa": ["Toi"],
    "GaGaGa": ["Espèce d'imbécile"],
    "Bu": ["Oui", "Eau"],
    "BuGa": ["Petite pompe"],
    "BuGaGa": ["Grosse pompe"],
    "Zo": ["Lui", "Extérieur", "Nouille"],
    "ZoBuGa": ["Pomper avec une petite pompe"],
    "ZoBuBuGa": ["Pomper avec une grosse pompe"],
    "ZoZo": ["Indépendant", "Nouilles"],
    "Meu": ["Trou"],
    "MeuMeu": ["Trous"],
    "MeuGaBu": ["Passoire"],
    "MeuMeuMeuMeuMeu": ["Fin"],
}
