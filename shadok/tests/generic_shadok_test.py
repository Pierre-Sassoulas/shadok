import itertools
from unittest import TestCase

from shadok import ShadokString
from shadok.language import Symbol


def all_capitalization(word):
    return list(
        map(
            "".join,
            itertools.product(
                *((character.upper(), character.lower()) for character in word)
            ),
        )
    )


class GenericShadokTest(TestCase):
    def setUp(self):
        raw_combinations = lambda word: all_capitalization(word.name)
        shadok_string_combination = lambda word: [
            ShadokString(combination) for combination in raw_combinations(word)
        ]
        self.gas = shadok_string_combination(Symbol.GA)
        self.gas_raw = raw_combinations(Symbol.GA)
        self.bus = shadok_string_combination(Symbol.BU)
        self.bus_raw = raw_combinations(Symbol.BU)
        self.zos = shadok_string_combination(Symbol.ZO)
        self.zos_raw = raw_combinations(Symbol.ZO)
        self.meus = shadok_string_combination(Symbol.MEU)
        self.meus_raw = raw_combinations(Symbol.MEU)
        self.words = {
            "Ga": ["{ga}"],
            "GaGa": ["{ga}{ga}"],
            "GaGaGa": ["{ga}{ga}{ga}"],
            "Bu": ["{bu}"],
            "BuGa": ["{bu}{ga}"],
            "BuGaGa": ["{bu}{ga}{ga}"],
            "Zo": ["{zo}"],
            "ZoBuGa": ["{zo}{bu}{ga}"],
            "ZoBuBuGa": ["{zo}{bu}{bu}{ga}"],
            "MeuGaBu": ["{meu}{ga}{bu}"],
            "MeuMeuMeuMeuMeu": ["{meu}{meu}{meu}{meu}{meu}"],
            "Ga GaGAga": ["{ga}", "{ga}{ga}{ga}"],
        }
        formatted = {}
        gabuzomeu_format = {
            "ga": Symbol.GA.value,
            "bu": Symbol.BU.value,
            "zo": Symbol.ZO.value,
            "meu": Symbol.MEU.value,
        }
        for key, words in self.words.items():
            formatted[key] = []
            for word in words:
                formatted[key].append(word.format(**gabuzomeu_format))
        self.words = formatted
