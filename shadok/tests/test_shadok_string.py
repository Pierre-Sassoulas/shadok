from shadok import ShadokInteger, ShadokString
from shadok.magic_faucet import MagicFaucet
from shadok.tests.generic_shadok_test import GenericShadokTest


class TestShadokString(GenericShadokTest):
    def test_init_from_integer(self):
        integers = [1, 8, 15, 33, 539, 143, 27]  # 4263407647244060364,]
        for i in integers:
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
