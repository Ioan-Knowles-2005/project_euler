# Anagramic Squares
# By replacing each of the letters in the word CARE with 1, 2, 9, 6 respectively we form a square number: 1296 = 36^2.
# What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 96^2
# We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted,
#  neither may a different letter have the same digital value as another letter.
# Using problem_98_words.txt find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).
# What is the largest square number formed by any member of such a pair?

import math
from collections import defaultdict

def read_words(filename):
    """Reads words from the given text file, returning them as a list of strings."""
    with open(filename, 'r') as f:
        text = f.read().strip()
    # The file typically has comma-separated words in quotes, e.g. "CARE","RACE",...
    # We remove quotes and split by comma
    words = text.replace('"', '').split(',')
    return words

def build_pattern(s):
    """
    Returns a list representing the "pattern" of s.
    Example:
      s = "CARE" => distinct letters => pattern [0,1,2,3]
      s = "MAMA" => pattern [0,1,0,1]
    """
    mapping = {}
    pattern = []
    next_id = 0
    for ch in s:
        if ch not in mapping:
            mapping[ch] = next_id
            next_id += 1
        pattern.append(mapping[ch])
    return tuple(pattern)

def solve_anagramic_squares(filename="words.txt"):
    words = read_words(filename)

    # 1) Group words by sorted letters => find anagram sets
    anagram_groups = defaultdict(list)
    for w in words:
        signature = ''.join(sorted(w))
        anagram_groups[signature].append(w)

    # We'll only need groups with at least 2 words
    anagram_groups = {k:v for k,v in anagram_groups.items() if len(v) >= 2}

    # 2) Precompute squares by length and group them by "digit pattern".
    #    We'll consider squares up to 10^10 if needed, but realistically words won't exceed length 10.
    #    Actually, the largest word length is ~14 in the default word list. We can handle up to length 14 => squares < 10^14.
    #    That's up to 3162277... which is too large to brute force. But typical puzzle has words up to length ~10.
    #    We'll handle squares up to 10^12 (1 million^2). That's enough for typical Euler #98. 
    #    Or we can just handle squares up to length 14 digits => 10^14 => sqrt=10^7 => 10 million squares is big but borderline feasible in optimized code.
    #
    #    A more typical approach: we only need squares up to length = max word length in the input.
    
    max_len = max(len(w) for w in words)
    # The largest integer with 'max_len' digits is 10^max_len -1
    # so the largest square needed is at most 10^max_len -1
    # => sqrt(10^max_len -1) ~ 10^(max_len/2)
    upper_bound = 10**(max_len)
    limit = int(math.isqrt(upper_bound - 1)) + 1  # a bit over

    # squares_by_length[d] = list of squares with d digits
    squares_by_length = defaultdict(list)
    for n in range(1, limit):
        sq = n*n
        s = str(sq)
        squares_by_length[len(s)].append(s)

    # For quick membership check:
    # squares_set_by_length[d] = set of squares with d digits
    squares_set_by_length = {}
    for d, arr in squares_by_length.items():
        squares_set_by_length[d] = set(arr)

    # For each length, build pattern-> list of squares
    square_pattern_map = defaultdict(list)  # key = (length, pattern), value = list of squares (strings)
    for d, sq_list in squares_by_length.items():
        for sq_str in sq_list:
            p = build_pattern(sq_str)
            square_pattern_map[(d, p)].append(sq_str)

    # 3) For each anagram group, look at all pairs of words in it, and attempt pattern matching
    best_square = 0

    for signature, group in anagram_groups.items():
        # We'll consider all pairs in this group
        # If the group is large, we have multiple pairs to check
        # For each pair, we'll do the pattern approach
        # We'll store word -> pattern once for efficiency
        word_pattern_cache = {}
        for w in group:
            word_pattern_cache[w] = build_pattern(w)

        # We'll check all distinct pairs
        from itertools import combinations
        for w1, w2 in combinations(group, 2):
            lenw = len(w1)  # same as len(w2)
            p1 = word_pattern_cache[w1]
            p2 = word_pattern_cache[w2]

            # We'll see if p1 is in square_pattern_map for length = lenw
            # If so, we try each candidate square that matches p1
            # Then we attempt a letter->digit mapping, check leading zero, apply to w2
            # If that yields a valid square in squares_set_by_length[lenw], record
            squares_for_p1 = square_pattern_map.get((lenw, p1), [])
            if not squares_for_p1:
                continue

            # For each candidate square that matches p1
            for sq_str1 in squares_for_p1:
                # Build letter->digit mapping from w1 -> sq_str1
                # e.g. w1='CARE', sq_str1='1296'
                mapping = {}
                used_digits = set()
                valid_map = True
                for ch, digit_char in zip(w1, sq_str1):
                    d = int(digit_char)
                    if ch in mapping:
                        if mapping[ch] != d:
                            valid_map = False
                            break
                    else:
                        # If d is already used for a different letter => conflict
                        if d in used_digits:
                            valid_map = False
                            break
                        mapping[ch] = d
                        used_digits.add(d)
                # Also check leading digit not zero
                if mapping[w1[0]] == 0:
                    valid_map = False

                if not valid_map:
                    continue

                # Now apply mapping to w2
                # If w2's first letter maps to 0 => invalid
                if mapping.get(w2[0], -1) == 0:
                    continue

                # If w2 has a letter not in mapping, we can't proceed
                # Actually, that shouldn't happen because w2 has same letters as w1 except possibly rearranged
                # But let's be safe
                sq2_list = []
                for ch in w2:
                    if ch not in mapping:
                        valid_map = False
                        break
                    sq2_list.append(str(mapping[ch]))

                if not valid_map:
                    continue

                sq_str2 = "".join(sq2_list)

                # Check if sq_str2 is in squares_set_by_length[lenw]
                if sq_str2 in squares_set_by_length[lenw]:
                    # We found a valid pair
                    val1 = int(sq_str1)
                    val2 = int(sq_str2)
                    best_square = max(best_square, val1, val2)

    return best_square

def main():
    filename = "words.txt"  # Change if needed
    answer = solve_anagramic_squares(filename)
    print("Largest square in any valid anagram pair is:", answer)

if __name__=="__main__":
    main()
