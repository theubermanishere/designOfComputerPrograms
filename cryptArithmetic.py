import itertools
import re

def valid(f):
    try:
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False

def solve(formula):
    for instance in fill_in(formula):
        if valid(instance):
            return instance
    return None

def fill_in(formula):
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    for digits in itertools.permutations('1234567890', len(letters)):
        table = str.maketrans(letters, ''.join(digits))
        yield formula.translate(table)

print(solve("ODD + ODD == EVEN"))
