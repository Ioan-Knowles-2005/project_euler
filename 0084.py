# Monopoly Odds
import math

def monopoly_with_d4_dice():
    """
    Solve the 'two 4-sided dice' variant of the Monopoly problem.
    Returns a string of the 3 most likely squares in 2-digit form, concatenated (the 'modal string').
    """

    # ----------------------------------
    # 1) Board Setup & Helper Structures
    # ----------------------------------

    N_SQUARES = 40

    # Define special squares
    GO = 0
    JAIL = 10
    G2J = 30  # "Go To Jail"
    CC_SQUARES = {2, 17, 33}
    CH_SQUARES = {7, 22, 36}
    
    # Railways and Utilities for CH cards
    RAILWAYS = [5, 15, 25, 35]
    UTILITIES = [12, 28]
    
    # Community Chest deck (16 cards).
    # We only care about the cards that move you:
    #  - 1 card: Advance to GO
    #  - 1 card: Go to JAIL
    # The other 14 do nothing (stay in place).
    # We'll encode them as a list of functions that transform (sq -> newSq).
    # Then the deck index cycles.
    def cc_card_advance_to_go(sq): return GO
    def cc_card_go_to_jail(sq):    return JAIL
    def cc_card_no_move(sq):       return sq
    
    CC_DECK = (
        [cc_card_advance_to_go, cc_card_go_to_jail] +
        [cc_card_no_move]*14
    )
    
    # Chance deck (16 cards).
    # 10 cards move you:
    #   1) Advance to GO
    #   2) Go to JAIL
    #   3) Go to C1 (sq=11)
    #   4) Go to E3 (sq=24)
    #   5) Go to H2 (sq=39)
    #   6) Go to R1 (sq=5)
    #   7,8) Go to next R
    #   9) Go to next U
    #   10) Go back 3 squares
    # The other 6 do nothing.
    def ch_card_advance_to_go(sq): return GO
    def ch_card_go_to_jail(sq):    return JAIL
    def ch_card_go_to_c1(sq):      return 11
    def ch_card_go_to_e3(sq):      return 24
    def ch_card_go_to_h2(sq):      return 39
    def ch_card_go_to_r1(sq):      return 5
    
    def ch_card_go_to_next_r(sq):
        # next railway from sq
        # squares of railways: 5,15,25,35 => pick the next one
        for r in RAILWAYS:
            if r > sq:
                return r
        # wrap around
        return RAILWAYS[0]
    
    def ch_card_go_to_next_u(sq):
        # next utility from sq
        # squares of utilities: 12,28
        for u in UTILITIES:
            if u > sq:
                return u
        # wrap
        return UTILITIES[0]
    
    def ch_card_go_back_3(sq):
        return (sq - 3) % N_SQUARES
    
    def ch_card_no_move(sq):
        return sq
    
    CH_DECK = (
        [
            ch_card_advance_to_go,
            ch_card_go_to_jail,
            ch_card_go_to_c1,
            ch_card_go_to_e3,
            ch_card_go_to_h2,
            ch_card_go_to_r1,
            ch_card_go_to_next_r,
            ch_card_go_to_next_r,
            ch_card_go_to_next_u,
            ch_card_go_back_3
        ]
        + [ch_card_no_move]*6
    )
    
    # ----------------------------------
    # 2) State Space Definition
    # ----------------------------------
    # We'll track: (square, consecutiveDoubles, ccIndex, chIndex)
    # consecutiveDoubles in {0,1,2}
    # ccIndex in {0..15}, chIndex in {0..15}
    
    def encode_state(sq, cd, cc_i, ch_i):
        return (sq
                + N_SQUARES * (cd
                + 3 * (cc_i
                + 16 * ch_i)))
    
    def decode_state(idx):
        # inverse of encode_state
        sq_part = idx % N_SQUARES
        rem = idx // N_SQUARES
        cd_part = rem % 3
        rem2 = rem // 3
        cc_part = rem2 % 16
        ch_part = rem2 // 16
        return (sq_part, cd_part, cc_part, ch_part)
    
    TOTAL_STATES = N_SQUARES * 3 * 16 * 16
    
    # Build a list of all possible dice outcomes for two 4-sided dice
    # Each outcome has probability 1/16
    dice_outcomes = []
    for d1 in range(1,5):
        for d2 in range(1,5):
            dice_outcomes.append((d1,d2))
    
    # ----------------------------------
    # 3) Transition Function
    # ----------------------------------
    # Given a state, we want a dictionary {nextState: probability}.
    # We'll build it on-the-fly for each iteration OR we can precompute it.
    
    from collections import defaultdict
    
    def next_square_after_chains(start_sq, cc_i, ch_i):
        """
        From 'start_sq', apply repeated logic for:
         - G2J => go to jail
         - CC => draw card
         - CH => draw card
         - 'go back 3 squares' from a CH card might land on CC/CH/G2J again, so we loop.
        Returns (finalSquare, newCC_i, newCH_i).
        """
        sq = start_sq
        cur_cc_i = cc_i
        cur_ch_i = ch_i
        
        while True:
            # 1) If G2J => go to jail
            if sq == G2J:
                sq = JAIL
                break
            
            # 2) If Community Chest => draw top card
            if sq in CC_SQUARES:
                card_fn = CC_DECK[cur_cc_i]
                cur_cc_i = (cur_cc_i + 1) % 16
                new_sq = card_fn(sq)
                if new_sq != sq:
                    # Moved
                    sq = new_sq
                    # If that leads to G2J or CH or CC, we must keep looping
                    # so continue
                    continue
                else:
                    # no move
                    break
            
            # 3) If Chance => draw top card
            elif sq in CH_SQUARES:
                card_fn = CH_DECK[cur_ch_i]
                cur_ch_i = (cur_ch_i + 1) % 16
                new_sq = card_fn(sq)
                if new_sq != sq:
                    sq = new_sq
                    # again, might need to loop
                    continue
                else:
                    break
            
            # Otherwise no special square => done
            break
        
        return (sq, cur_cc_i, cur_ch_i)
    
    # We'll build a transition dictionary: trans[state] = {nextState: prob, ...}
    # But because we have 30,720 states, we can store it as a list of dicts or similar.
    
    trans = [defaultdict(float) for _ in range(TOTAL_STATES)]
    
    for s_idx in range(TOTAL_STATES):
        sq, cd, cc_i, ch_i = decode_state(s_idx)
        
        # For each dice outcome
        for (d1, d2) in dice_outcomes:
            sum_d = d1 + d2
            # check doubles
            if d1 == d2:
                new_cd = cd + 1
            else:
                new_cd = 0
            
            if new_cd == 3:
                # 3 consecutive doubles => go to jail immediately
                fsq = JAIL
                fcc_i = cc_i
                fch_i = ch_i
                new_cd = 0
            else:
                # normal move
                moved_sq = (sq + sum_d) % N_SQUARES
                # if landed on G2J => will eventually go to jail, or if landed on CH/CC => might move
                fsq, fcc_i, fch_i = next_square_after_chains(moved_sq, cc_i, ch_i)
            
            ns_idx = encode_state(fsq, new_cd, fcc_i, fch_i)
            trans[s_idx][ns_idx] += 1.0 / 16.0
    
    # ----------------------------------
    # 4) Iteratively Find Steady-State
    # ----------------------------------
    
    import math
    
    # Probability vector: prob[state] for each state
    prob_old = [0.0]*TOTAL_STATES
    # Start at (sq=0, cd=0, cc_i=0, ch_i=0) with probability 1
    start_idx = encode_state(0,0,0,0)
    prob_old[start_idx] = 1.0
    
    # We'll do repeated multiplication by transition matrix until it converges
    # Because the chain is finite and aperiodic, it will converge.
    
    epsilon = 1e-15
    while True:
        prob_new = [0.0]*TOTAL_STATES
        # For each state s, distribute its prob to next states
        for s_idx in range(TOTAL_STATES):
            p_s = prob_old[s_idx]
            if p_s > 0:
                for ns_idx, w in trans[s_idx].items():
                    prob_new[ns_idx] += p_s * w
        
        # Check for convergence
        diff = 0.0
        for i in range(TOTAL_STATES):
            diff += abs(prob_new[i] - prob_old[i])
        prob_old = prob_new
        
        if diff < epsilon:
            break
    
    # Now prob_old is effectively the steady-state distribution
    # ----------------------------------
    # 5) Aggregate Probabilities by Square
    # ----------------------------------
    square_probs = [0.0]*N_SQUARES
    for s_idx in range(TOTAL_STATES):
        p = prob_old[s_idx]
        sq, cd, cc_i, ch_i = decode_state(s_idx)
        square_probs[sq] += p
    
    # ----------------------------------
    # 6) Find the Top 3 Squares & Build Modal String
    # ----------------------------------
    # We want squares in descending order of probability.
    # Then take the top 3, and produce 6-digit string "XXYYZZ".
    
    indexed_probs = list(enumerate(square_probs))
    indexed_probs.sort(key=lambda x: x[1], reverse=True)
    
    top3 = indexed_probs[:3]
    # Each is (squareIndex, probability)
    # Sort them by probability descending, tie-break by square index if needed
    # We want the squares in order of descending probability:
    #  Then produce "square0 square1 square2" in 2-digit form each.
    
    # If squares tie, we still list them in that order. 
    # Usually there's a distinct top 3, though.
    
    def two_digit(n):
        return f"{n:02d}"
    
    top3_squares = [sq for (sq, prob) in top3]
    
    # build the string
    modal_string = "".join(two_digit(sq) for sq in top3_squares)
    return modal_string


result = monopoly_with_d4_dice()
print("Modal string for Monopoly with two 4-sided dice:", result)