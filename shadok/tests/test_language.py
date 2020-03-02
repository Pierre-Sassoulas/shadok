from shadok import ImproperShadokSyntax, ShadokString
from shadok.language import Symbol
from shadok.magic_faucet import MagicFaucet
from shadok.tests.generic_shadok_test import GenericShadokTest


class TestLanguage(GenericShadokTest):
    def test_normalize_one_word(self):
        for ga in self.gas_raw:
            self.assertEqual(MagicFaucet.normalize(ga), [Symbol.GA.value])
        for bu in self.bus_raw:
            self.assertEqual(MagicFaucet.normalize(bu), [Symbol.BU.value])
        for zo in self.zos_raw:
            self.assertEqual(MagicFaucet.normalize(zo), [Symbol.ZO.value])
        for meu in self.meus_raw:
            self.assertEqual(MagicFaucet.normalize(meu), [Symbol.MEU.value])

    def test_pretty_print_one_word(self):
        for ga in self.gas:
            self.assertEqual(str(ga), "Ga")
        for bu in self.bus:
            self.assertEqual(str(bu), "Bu")
        for zo in self.zos:
            self.assertEqual(str(zo), "Zo")
        for meu in self.meus:
            self.assertEqual(str(meu), "Meu")

    def test_normalize_multiple_words(self):
        for word in self.words:
            result = MagicFaucet.normalize(word)
            expected = self.words[word]
            self.assertEqual(
                result,
                expected,
                "Normalized string '%s' is not what was expected ('%s')"
                % (result, expected),
            )

    def test_pretty_print_multiple_words(self):
        test_values = {
            "MeUGAbu": "MeuGaBu",
            "MeuMeu MeuMEUMeu": "MeuMeu MeuMeuMeu",
            "Ga GaGAga": "Ga GaGaGa",
        }
        for value, expected in test_values.items():
            self.assertEqual(str(ShadokString(value)), expected)

    def test_improper_syntax(self):
        test_values = {
            "GaBOMu": """
Incorrect shadok syntax in 'GaBOMu'
                              ^^^^
""",
            "MAMA MMMEUMeu": """
Incorrect shadok syntax in 'MAMA'
                            ^^^^
""",
            "Ga! GaGAga": """
Incorrect shadok syntax in 'Ga!'
                              ^
""",
            "Ga42Ga": """
Incorrect shadok syntax in 'Ga42Ga'
                              ^^
""",
            "AGaGa": """
Incorrect shadok syntax in 'AGaGa'
                            ^
""",
            "GaBeuZoMu": """
Incorrect shadok syntax in 'GaBeuZoMu'
                              ^^^  ^^
""",
        }
        for value, expected in test_values.items():
            with self.assertRaises(ImproperShadokSyntax) as exc:
                ShadokString(value)
            self.assertIn(expected, str(exc.exception))
