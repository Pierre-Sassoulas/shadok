from shadok import ShadokInteger, ShadokString
from shadok.language import Symbol
from shadok.path_to_success import ImproperShadokLogic
from shadok.tests.generic_shadok_test import GenericShadokTest


class TestMathematics(GenericShadokTest):
    def test_int_value(self):
        for ga in self.gas:
            self.assertEqual(int(ga), 0)
        for bu in self.bus:
            self.assertEqual(int(bu), 1)
        for zo in self.zos:
            self.assertEqual(int(zo), 2)
        for meu in self.meus:
            self.assertEqual(int(meu), 3)

    def test_complicated_number(self):
        self.assertEqual(int(ShadokString("GaBu")), 1)
        self.assertEqual(int(ShadokString("ZoGa")), 8)
        self.assertEqual(int(ShadokString("MeuMeu")), 15)
        self.assertEqual(int(ShadokString("ZoGaBu")), 33)
        self.assertEqual(int(ShadokString("ZoGaBuZoMeu")), 539)
        self.assertEqual(int(ShadokString("ZoGaMeuMeu")), 143)
        self.assertEqual(int(ShadokString("BuZoMeu")), 27)
        # self.assertEqual(
        #    int(
        #        ShadokString(
        #            "MeuZoZoZoZoZoZoZoZoZoZoZoZoZoZoZoZoZoZoZoZoZoZoZoGaBuZoMeuZoZozo"
        #        )
        #    ),
        #    4263407647244060364,
        # )
        gbzm = {
            "g": Symbol.GA_DIGIT.value,
            "b": Symbol.BU_DIGIT.value,
            "z": Symbol.ZO_DIGIT.value,
            "m": Symbol.MEU_DIGIT.value,
        }
        self.assertEqual(str(ShadokString(1)), "{b}".format(**gbzm))
        self.assertEqual(str(ShadokString(8)), "{z}{g}".format(**gbzm))
        self.assertEqual(str(ShadokString(15)), "{m}{m}".format(**gbzm))
        self.assertEqual(str(ShadokString(33)), "{z}{g}{b}".format(**gbzm))
        self.assertEqual(str(ShadokString(539)), "{z}{g}{b}{z}{m}".format(**gbzm))
        self.assertEqual(str(ShadokString(143)), "{z}{g}{m}{m}".format(**gbzm))
        self.assertEqual(str(ShadokString(27)), "{b}{z}{m}".format(**gbzm))
        # self.assertEqual(
        #    str(ShadokString(4263407647244060364)),
        #    "{m}{z}{z}{z}{z}{z}{z}{z}{z}{z}{z}{z}{z}{z}{z}{z}{z}{z}{z}{z}{z}{z}{z}{z}{g}{b}{z}{m}{z}{z}{z}".format(
        #        **gbzm
        #    ),
        # )
        self.assertEqual(ShadokInteger(1).pronunciation, "Bu")
        self.assertEqual(ShadokInteger(8).pronunciation, "ZoGa")
        self.assertEqual(ShadokInteger(15).pronunciation, "MeuMeu")
        self.assertEqual(ShadokInteger(33).pronunciation, "ZoGaBu")
        self.assertEqual(ShadokInteger(539).pronunciation, "ZoGaBuZoMeu")
        self.assertEqual(ShadokInteger(143).pronunciation, "ZoGaMeuMeu")
        self.assertEqual(ShadokInteger(27).pronunciation, "BuZoMeu")
        # self.assertEqual(
        #    ShadokInteger(4263407647244060364).pronunciation,
        #    "MeuZoZoZoZoZoZoZoZoZoZoZoZoZoZoZoZoZoZoZoZoZoZoZoGaBuZoMeuZoZoZo",
        # )

    def test_impossible_cast_to_int(self):
        with self.assertRaises(ImproperShadokLogic) as err:
            int(ShadokString("GabuBu zoMeu"))
        self.assertIn(
            "Cannot cast string containing multiple words ('GabuBu zoMeu') to an int.",
            str(err.exception),
        )

    def test_impossible_initialisation(self):
        with self.assertRaises(ImproperShadokLogic) as err:
            ShadokInteger("GaZo BuMeu")
        self.assertIn(
            "Cannot cast string containing multiple words ('GaZo BuMeu') to an int.",
            str(err.exception),
        )
        with self.assertRaises(ImproperShadokLogic) as err:
            ShadokInteger(ImproperShadokLogic())
        self.assertIn(
            "Can only create a ShadokInteger from a str or an int, not a 'ImproperShadokLogic'",
            str(err.exception),
        )
