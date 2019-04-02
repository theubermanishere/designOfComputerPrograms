import itertools
import re

def valid(f):
    try:
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False

def solve(formula):
    for combo in itertools.permutations('0123456789', 5):
        table = str.maketrans('ODEVN', ''.join(list(map(str, combo))))
        if valid(formula.translate(table)):
            return formula.translate(table)
    return None

print(solve("ODD + ODD == EVEN"))
