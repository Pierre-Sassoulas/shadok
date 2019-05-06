from shadok.language import Symbol
from shadok.magic_faucet import MagicFaucet
from shadok.mathematic import human_to_shadok_digit, shadok_to_human_digit
from shadok.path_to_success import ImproperShadokLogic


class ShadokInteger:
    def __init__(self, value):
        if isinstance(value, str):
            normalized_string = MagicFaucet.normalize(value)
            if len(normalized_string) > 1:
                raise ImproperShadokLogic(
                    "Cannot cast string containing multiple words ('%s') to an int."
                    % value
                )
            int_value = self.shadok_number_to_int(normalized_string[0])
        elif isinstance(value, int):
            int_value = value
        else:
            raise ImproperShadokLogic(
                "Can only create a ShadokInteger from a str or an int, not a '%s'"
                % type(value).__name__
            )
        self.value = int_value

    def shadok_number_to_int(self, number):
        n = len(number)
        factor = 1
        r = 0
        for i in range(n):
            digit = number[n - i - 1]
            r += factor * shadok_to_human_digit(digit)
            factor *= 4
        return r

    def int_to_shadok_number(self):
        number = []
        n = self.value
        factor = 1
        while n / factor >= 1:
            factor *= 4
        factor /= 4
        while factor >= 1:
            dividende = int(n // factor)
            number.append(human_to_shadok_digit(dividende))
            n -= dividende * factor
            factor /= 4
        return "".join(number)

    def __repr__(self):
        return self.int_to_shadok_number()

    def __str__(self):
        return self.__repr__()

    @property
    def pronunciation(self):
        result = ""
        conversion = {
            Symbol.GA_DIGIT.value: "Ga",
            Symbol.BU_DIGIT.value: "Bu",
            Symbol.ZO_DIGIT.value: "Zo",
            Symbol.MEU_DIGIT.value: "Meu",
        }
        for char in str(self):
            result += conversion.get(char)
        return result

    def __int__(self):
        return self.value
