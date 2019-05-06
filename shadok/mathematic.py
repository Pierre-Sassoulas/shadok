from shadok.language import Symbol

_shadok_to_human = {
    Symbol.GA.value: 0,
    Symbol.BU.value: 1,
    Symbol.ZO.value: 2,
    Symbol.MEU.value: 3,
    Symbol.GA_DIGIT.value: 0,
    Symbol.BU_DIGIT.value: 1,
    Symbol.ZO_DIGIT.value: 2,
    Symbol.MEU_DIGIT.value: 3,
}

__human_to_shadok = {
    0: Symbol.GA_DIGIT.value,
    1: Symbol.BU_DIGIT.value,
    2: Symbol.ZO_DIGIT.value,
    3: Symbol.MEU_DIGIT.value,
}


def shadok_to_human_digit(letter):
    return _shadok_to_human[letter]


def human_to_shadok_digit(integer):
    return __human_to_shadok[integer]
