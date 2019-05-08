from shadok.magic_faucet import MagicFaucet
from shadok.shadok_integer import ShadokInteger


class ShadokString(str):
    def __init__(self, input_string):
        """ Standardized shadok string.

        :param input_string: A string containing correct shadok syntax, a ShadokString, a ShadokInt or an int.
        """
        #  print("Creating a shadok string from : '%s' (a %s)" % (input, input.__class__.__name__))
        if isinstance(input_string, str):
            # ShadokString ARE string
            self.raw_string = input_string
        elif isinstance(input_string, int):
            shadok_int = ShadokInteger(input_string)
            self.raw_string = str(shadok_int)
        elif isinstance(input_string, ShadokInteger):
            self.raw_string = str(input_string)
        else:
            msg = "Can only create a 'ShadokString' from an int, "
            msg += "a string containing correct shadok syntax, "
            msg += "a ShadokInteger, or a ShadokString, "
            msg += "not from a '%s'" % input_string.__class__.__name__
            raise ValueError(msg)
        if self.raw_string != "":
            MagicFaucet.check_syntax(self.raw_string)
        self.normalized_string = MagicFaucet.normalize(self.raw_string)
        super(ShadokString, self).__init__()

    def __repr__(self):
        return MagicFaucet.pretty_print(self.raw_string)

    def __str__(self):
        return self.__repr__()

    def __int__(self):
        number = ShadokInteger(self.raw_string)
        return int(number)

    def __bool__(self):
        return bool(int(self))
