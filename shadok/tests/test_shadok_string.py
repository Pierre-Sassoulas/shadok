from shadok import ShadokInteger, ShadokString
from shadok.magic_faucet import MagicFaucet
from shadok.tests.generic_shadok_test import GenericShadokTest
from shadok.path_to_success import ImproperShadokSyntax


class TestShadokString(GenericShadokTest):
    def setUp(self):
        self.integers = [1, 8, 15, 33, 539, 143, 27]  # 4263407647244060364,]

    def test_init_from_integer(self):
        for i in self.integers:
            shadok_string_from_integer = ShadokString(i)
            self.assertEqual(int(shadok_string_from_integer), i)
            shadok_integer = ShadokInteger(i)
            self.assertEqual(int(shadok_integer), i)
            shadok_string_from_shadok_integer = ShadokString(shadok_integer)
            self.assertEqual(int(shadok_string_from_shadok_integer), i)

    def test_init_from_wrong_object(self):
        with self.assertRaises(ValueError) as err:
            ShadokString(MagicFaucet())
        self.assertIn("MagicFaucet", str(err.exception))

    def test_init_from_shadok_string(self):
        string = ShadokString("BuGaZoMeu")
        other_shadok_string = ShadokString(string)
        self.assertEqual(string.raw_string, other_shadok_string.raw_string)

    def test_check_syntax(self):
        with self.assertRaises(ValueError) as err:
            MagicFaucet.check_syntax(MagicFaucet())
        self.assertIn(
            "MagicFaucet.check_syntax(test:str) can only handle string not MagicFaucet.",
            str(err.exception),
        )

    def test_add(self):
        test_values = {"bu": "BuGAMeu", "BU Ga": " BuGAMeu"}
        for initial, added in test_values.items():
            shadok_string = ShadokString(initial)
            shadok_string += added
            self.assertEqual(str(shadok_string), str(ShadokString(initial + added)))
        test_values_with_syntax_error = [
            {
                "initial": "bu ",
                "added": "  Bu GaMeuh",
                "expected": """
Incorrect shadok syntax in 'GaMeuh'
                                 ^
""",
            },
            {
                "initial": "BU Ga",
                "added": " Gibi",
                "expected": """
Incorrect shadok syntax in 'Gibi'
                            ^^^^
""",
            },
        ]
        for test_value_with_syntax_error in test_values_with_syntax_error:
            shadok_string = ShadokString(test_value_with_syntax_error["initial"])
            with self.assertRaises(ImproperShadokSyntax) as err:
                shadok_string += test_value_with_syntax_error["added"]
            self.assertIn(test_value_with_syntax_error["expected"], str(err.exception))

    def test_bool(self):
        for i in self.integers:
            shadok_string = ShadokString(i)
            self.assertEqual(bool(shadok_string), True)
        for i in ["", 0, "Ga"]:
            shadok_string = ShadokString(i)
            self.assertEqual(bool(shadok_string), False)
