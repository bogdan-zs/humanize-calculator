from functools import lru_cache
import re

OPERATORS = {
    '+': 'plus',
    '-': 'minus',
    '*': 'multiply',
    '/': 'divided by',
    '=': 'equals'
}
DIGITS = ['zero', 'one', 'two', 'three', 'four',
          'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
          'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
          'eighteen', 'nineteen']
TENS = ['', '', 'twenty', 'thirty', 'forty',
        'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
INVALID_MESSAGE = 'invalid input'
DIGIT_REGEX = r'\d{1,12}'
MAX_LEN_NUMBER_TO_INFO = {
    3: {
        'pow10': 2,
        'grade_name': 'hundred'
    },
    6: {
        'pow10': 3,
        'grade_name': 'thousand'
    },
    9: {
        'pow10': 6,
        'grade_name': 'million'
    },
    12: {
        'pow10': 9,
        'grade_name': 'billion'
    }
}


def all(array, func=lambda x: x):
    """Return true if all elements is true else will return false"""
    for el in array:
        if not func(el):
            return False
    return True


def is_digit(x):
    return bool(re.match(DIGIT_REGEX, x))


@lru_cache()
def convert_nn(number):
    """Convert number from 20 to 99 to human readable number"""
    if TENS[number // 10]:
        return TENS[number // 10] + '-' + DIGITS[number % 10]
    else:
        return DIGITS[number % 10]


@lru_cache()
def humanize_number(number):
    if number == '0':
        return ''
    str_number = number[1:] if number[0] == '0' else number
    number = int(str_number)
    if number < len(DIGITS):
        return DIGITS[number]
    if len(str_number) <= 2:
        return convert_nn(number)
    else:
        for max_len, info in MAX_LEN_NUMBER_TO_INFO.items():
            if len(str_number) <= max_len:
                return ' '.join([
                    humanize_number(str(number // 10 ** info['pow10'])),
                    info['grade_name'],
                    humanize_number(str(number % 10 ** info['pow10']))]).strip()


def humanize_calculator(expretion):
    operators_and_operands = re.split(r'\s+', expretion)
    res = []

    if not all(operators_and_operands, lambda op: op in OPERATORS or is_digit(op)):
        return INVALID_MESSAGE

    for op in operators_and_operands:
        if is_digit(op):
            res.append(humanize_number(op))
        else:
            res.append(OPERATORS[op])
    return ' '.join(res)
