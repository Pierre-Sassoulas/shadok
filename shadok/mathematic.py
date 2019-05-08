from shadok.language import Symbol

_SHADOK_TO_HUMAN = {
    Symbol.GA.value: 0,
    Symbol.BU.value: 1,
    Symbol.ZO.value: 2,
    Symbol.MEU.value: 3,
    Symbol.GA_DIGIT.value: 0,
    Symbol.BU_DIGIT.value: 1,
    Symbol.ZO_DIGIT.value: 2,
    Symbol.MEU_DIGIT.value: 3,
}

__HUMAN_TO_SHADOK = {
    0: Symbol.GA_DIGIT.value,
    1: Symbol.BU_DIGIT.value,
    2: Symbol.ZO_DIGIT.value,
    3: Symbol.MEU_DIGIT.value,
}


def shadok_to_human_digit(letter):
    return _SHADOK_TO_HUMAN[letter]


def human_to_shadok_digit(integer):
    return __HUMAN_TO_SHADOK[integer]
