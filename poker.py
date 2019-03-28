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
