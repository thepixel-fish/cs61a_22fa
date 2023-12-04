import sqlite3

points = {'A': 1, 'J': 10, 'Q': 10, 'K': 10}
points.update({n: n for n in range(2, 11)})

def hand_score(hand):
    f"""return the score of hand
    >>> hand_score(['A', 'J', 4])
    15
    >>> hand_score(['J', 6, 5])
    21
    """
    total = sum([points(card) for card in hand])
    if total  <= 11 and 'A' in hand:
        return total + 10
    return total

def deal
