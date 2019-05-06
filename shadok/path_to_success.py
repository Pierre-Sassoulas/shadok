""" Plus ça rate, plus on a de chances que ça marche."""


class ImproperShadokSyntax(Exception):
    def __init__(self, word, matches):
        base_message = "\nIncorrect shadok syntax in '"
        msg = "%s%s'" % (base_message, word)
        msg += "\n{}".format(" " * (len(base_message) - len("'")))
        chevrons = []
        for i in range(len(word)):
            chevrons.append("^")
        for match in matches:
            for i in range(*match.span()):
                chevrons[i] = " "
        for chevron in chevrons:
            msg += chevron
        msg += "\nAu Goulp !"
        super(ImproperShadokSyntax, self).__init__(msg)


class ImproperShadokLogic(Exception):
    pass


class ColanderIsInFactABusError(Exception):
    pass


class ShadokUpholdingPlanetError(Exception):
    pass


class ShadokBurntByGegeneError(Exception):
    pass
