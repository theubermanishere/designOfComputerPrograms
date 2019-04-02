# Solution for Zebra Puzzle [https://en.wikipedia.org/wiki/Zebra_Puzzle]

import itertools

def imRight(h1, h2):
    """ Procedure to check if h1 is immediately right of h2. """
    return h1 - h2 == 1

def nextTo(h1, h2):
    """ Procedure to check if h1 is next to h2. """
    return abs(h1 - h2) == 1

def zebra_puzzle():
    """ Procedure to solve the zebra puzzle by trying different
    combinations possible and checking their suitability.

    01. There are five houses.
    02. The Englishman lives in the red house.
    03. The Spaniard owns the dog.
    04. Coffee is drunk in the green house.
    05. The Ukrainian drinks tea.
    06. The green house is immediately to the right of the ivory house.
    07. The Old Gold smoker owns snails.
    08. Kools are smoked in the yellow house.
    09. Milk is drunk in the middle house.
    10. The Norwegian lives in the first house.
    11. The man who smokes Chesterfields lives in the house next to the man with the fox.
    12. Kools are smoked in the house next to the house where the horse is kept.
    13. The Lucky Strike smoker drinks orange juice.
    14. The Japanese smokes Parliaments.
    15. The Norwegian lives next to the blue house.

    Now, who drinks water? Who owns the zebra?
    """


    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))
    return next((WATER, ZEBRA)
            for (red, green, ivory, yellow, blue) in orderings
            if imRight(green, ivory) #6
            for (Englishman, Spaniard, Ukrainian, Japanese, Norweign) in orderings
            if Englishman is red #2
            if Norweign is first #10
            if nextTo(Norweign, blue) #15
            for (dog, snail, fox, horse, ZEBRA) in orderings
            if Spaniard is dog #3
            for (coffee, tea, milk, orangeJuice, WATER) in orderings
            if coffee is green #4
            if Ukrainian is tea #5
            if milk is middle #9
            for (oldGold, kools, chester, parliaments, luckyStrike) in orderings
            if oldGold is snail #7
            if kools is yellow #8
            if nextTo(chester, fox) #11
            if nextTo(kools, horse) #12
            if luckyStrike is orangeJuice #13
            if Japanese is parliaments #14
            )

if __name__ == "__main__":
    print("Water: {0}, Zebra: {1}".format(*zebra_puzzle()))
