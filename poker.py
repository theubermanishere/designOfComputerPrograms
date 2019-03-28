# Program for deciding a winner amongst players in a game of poker

def poker(hands):
    """Program to output the winning hands from all hands."""
    return max(hands, key=hand_rank)

def hand_rank(hand):
    """Return value indicating the rank of a hand."""
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):         # Straight Flush
        return 8
    elif nkind(ranks, 4):                       # 4 of a kind
        return 7
    elif nkind(ranks, 3) and nkind(ranks, 2):   # Full House
        return 6
    elif flush(hand):                           # Flush
        return 5
    elif straight(ranks):                       # Straight
        return 4
    elif nkind(ranks, 3):                       # 3 of a kind
        return 3
    elif pair(ranks):                           # Two pair
        return 2
    elif nkind(ranks, 2):                       # One pair
        return 1
    else:
        return 0                                # Nothing

def card_ranks(hand):
    """Returns the ranks of cards in sorted order."""
    return sorted([rank for rank,suit in hand], reverse=True)

def straight(ranks):
    """Returns True if ranks form a straight."""
    return len(set(ranks)) == 5 and (max(ranks) - min(ranks) == 4)

def flush(hand):
    """Returns True if the hand forms a flush."""
    return len(set([suit for _, suit in hand])) == 1

def nkind(ranks, n):
    """Returns True if a n-of-a-kind is present in ranks."""
    for i in set(ranks):
        if ranks.count(i) == n:
            return True
    return False

def twoPair(ranks):
    """Returns the two pair if present in the hand, else None."""
    pair = nkind(ranks, 2)
    lowpair = nkind(list(reversed(ranks)), 2)
    if pair != lowpair:
        return (pair, lowpair)
    else:
        return None

defaultDeck = [a+b for a in '23456789TJQKA' for s in 'SHDC']

def deal(numhands, n = 5, deck = defaultDeck):
    """Deals numhands hands of n cards from deck."""
    random.shuffle(deck)
    for i in range(numhands):
        yield deck[i*n:n*(i+1)]

if __name__ == '__main__':
    # TODO: Add Tests
