#Poker Hands
# The file, poker.txt, contains one-thousand random hands dealt to two players. 
# Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards
# and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards),
# each player's hand is in no specific order, and in each hand there is a clear winner.

#How many hands does Player 1 win?

from collections import Counter

values_map = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
              '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11,
              'Q': 12, 'K': 13, 'A': 14}

def hand_rank(hand):
    """
    Returns a tuple representing the rank of the hand.
    The tuple is structured so that a higher tuple means a better hand.
    """
    # Get the numeric values and sort them in descending order.
    values = sorted([values_map[card[0]] for card in hand], reverse=True)
    suits = [card[1] for card in hand]
    counts = Counter(values)
    freqs = sorted(counts.values(), reverse=True)  # e.g. [3,1,1] for three-of-a-kind
    # For tie-breakers, we want groups sorted by (frequency, value)
    groups = sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True)
    
    flush = len(set(suits)) == 1
    straight = (max(values) - min(values) == 4) and len(set(values)) == 5
    
    if straight and flush:
        return (8, max(values))
    if freqs[0] == 4:
        # Four of a kind: (7, rank of quad, kicker)
        four_val = groups[0][0]
        kicker = [v for v in values if v != four_val][0]
        return (7, four_val, kicker)
    if freqs[0] == 3 and freqs[1] == 2:
        # Full House: (6, rank of triple, rank of pair)
        three_val = groups[0][0]
        pair_val = groups[1][0]
        return (6, three_val, pair_val)
    if flush:
        return (5, values)
    if straight:
        return (4, max(values))
    if freqs[0] == 3:
        # Three of a Kind: (3, rank of triple, kickers sorted)
        three_val = groups[0][0]
        kickers = sorted([v for v in values if v != three_val], reverse=True)
        return (3, three_val, kickers)
    if freqs[0] == 2 and freqs[1] == 2:
        # Two Pairs: (2, higher pair, lower pair, kicker)
        pair_vals = sorted([item[0] for item in groups if item[1] == 2], reverse=True)
        kicker = [v for v in values if v not in pair_vals][0]
        return (2, pair_vals[0], pair_vals[1], kicker)
    if freqs[0] == 2:
        # One Pair: (1, rank of pair, kickers sorted)
        pair_val = groups[0][0]
        kickers = sorted([v for v in values if v != pair_val], reverse=True)
        return (1, pair_val, kickers)
    # High Card:
    return (0, values)

# Read the poker hands file.
player1_wins = 0
with open(r"C:\Users\ioank\OneDrive\Desktop\Project Euler\problem_54_poker_hands.txt") as f:
    for line in f:
        cards = line.split()
        hand1 = cards[:5]
        hand2 = cards[5:]
        if hand_rank(hand1) > hand_rank(hand2):
            player1_wins += 1

print(player1_wins)
