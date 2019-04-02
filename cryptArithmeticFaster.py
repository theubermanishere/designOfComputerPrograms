import itertools
import re

def compile_word(word):
    """ Compile a word of uppercase letters as numeric digits.
    E.g. compile_word('YOU') => '(1*U + 10*O + 100*Y)'
    Non-uppercase words unchanged. """
    if word.isupper():
        terms = [('%s*%s' % (10**i, d)) for (i, d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    else:
        return word

def faster_solve(formula):
    f, letters = compile_formula(formula)
    for digits in itertools.permutations((1,2,3,4,5,6,7,8,9,0), len(letters)):
        try:
            if f(*digits) is True:
                table = str.maketrans(letters, ''.join(map(str, digits)))
                return formula.translate(table)
        except ArithmeticeError:
            pass

def compile_formula(formula, verbose = False):
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    parms = ', '.join(letters)
    tokens = list(map(compile_word, re.split('([A-Z]+)', formula)))
    body = ''.join(tokens)
    f = 'lambda %s: %s' % (parms, body)
    if verbose: print(f)
    return eval(f), letters

print(faster_solve("ODD + ODD == EVEN"))


