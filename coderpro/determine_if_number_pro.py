# Valid Number
# A valid number can be split up into these components (in order):
# A decimal number or an integer.
# (Optional) An 'e' or 'E', followed by an integer.

# A decimal number can be split up into these components (in order):
# (Optional) A sign character (either '+' or '-').
# One of the following formats:
# One or more digits, followed by a dot '.'.
# One or more digits, followed by a dot '.', followed by one or more digits.
# A dot '.', followed by one or more digits.

# An integer can be split up into these components (in order):
# (Optional) A sign character (either '+' or '-').
# One or more digits.

# For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].
# Given a string s, return true if s is a valid number.

from enum import Enum

class DigitState(Enum):
    BEGIN = 0
    NEGATIVE1 = 1
    DIGIT1 = 2
    DOT = 3
    DIGIT2 = 4
    E = 5
    NEGATIVE2 = 6
    DIGIT3 = 7

STATE_VALIDATOR = {
    DigitState.BEGIN: lambda x: True,
    DigitState.DIGIT1: lambda x: x.isdigit(),
    DigitState.NEGATIVE1: lambda x: x == '-',
    DigitState.DIGIT2: lambda x: x.isdigit(),
    DigitState.DOT: lambda x: x == '.',
    DigitState.E: lambda x: x == 'e',
    DigitState.NEGATIVE2: lambda x: x == '-',
    DigitState.DIGIT3: lambda x: x.isdigit(),
}

NEXT_STATES_MAP = {
    DigitState.BEGIN: [DigitState.NEGATIVE1, DigitState.DIGIT1, DigitState.DOT],
    DigitState.NEGATIVE1: [DigitState.DIGIT1, DigitState.DOT],
    DigitState.DIGIT1: [DigitState.DIGIT1, DigitState.DOT, DigitState.E],
    DigitState.DOT: [DigitState.DIGIT2],
    DigitState.E: [DigitState.NEGATIVE2, DigitState.DIGIT3],
    DigitState.DIGIT2: [DigitState.DIGIT2, DigitState.E],
    DigitState.NEGATIVE2: [DigitState.DIGIT3],
    DigitState.DIGIT3: [DigitState.DIGIT3],
}


def parse_number(str):
    state = DigitState.BEGIN

    for c in str:
        found = False
        for next_state in NEXT_STATES_MAP[state]:
            if STATE_VALIDATOR[next_state](c):
                state = next_state
                found = True
                break
        if not found:
            return False

    return state in [DigitState.DIGIT1, DigitState.DIGIT2, DigitState.DIGIT3]

# solution below is simple but might not be accepted by interviewers
def isNumber(s):
        list1 = ['inf', '-inf', '+inf', 'infinity', '+infinity', '-infinity', 'Infinity', '+Infinity', '-Infinity']
        if s in list1:
            return False
        try:
            s = float(s)
            return True
        except ValueError:     
            return False


print(parse_number('12.3'))
# True
print(parse_number('12a'))
# False
print(parse_number('.123'))
# True
print('---')
print(isNumber('12.3'))
# True
print(isNumber('12a'))
# False
print(isNumber('.123'))
# True