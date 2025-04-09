# Amicable Chains
# The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, 14 
# which sum to 28 therefore we call it a perfect number.
# Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220 so we call these an amicable pair
# Perhaps less well known are longer chains. For example, starting with 12496 we form a chain of five numbers:
# 12496 -> 14288 -> 15472 -> 14536 -> 14264 -> 12496 -> ...
# Since this chain returns to its starting point, it is called an amicable chain.
# Find the smallest member of the longest amicable chain with no element exceeding one million

def sum_of_proper_divisors(limit):
    """
    Returns a list `sod` of length limit+1, where sod[n] is the sum of
    proper divisors of n, for 1 <= n <= limit.
    """
    sod = [1] * (limit + 1)  # sod[1] is dummy, but let's keep it for indexing
    sod[0] = 0  # not used
    
    # 1 is a proper divisor for all n>1, so we start from p=2
    for p in range(2, limit // 2 + 1):
        multiple = 2 * p
        while multiple <= limit:
            sod[multiple] += p
            multiple += p
    
    sod[1] = 0  # sum of proper divisors of 1 is 0
    return sod

def find_longest_amicable_chain(limit=1_000_000):
    """
    Finds the smallest member of the longest amicable chain with all elements <= limit.
    Returns (smallest_member, chain_length).
    """
    # Precompute sum of proper divisors for all n <= limit
    sod = sum_of_proper_divisors(limit)

    visited_global = [False] * (limit + 1)  # To skip re-processing
    max_length = 0
    best_smallest_member = None
    
    # Explore each number
    for start in range(2, limit + 1):
        if visited_global[start]:
            continue
        
        # Build the sequence from `start`
        chain = []
        index_map = {}  # number -> index in `chain`
        current = start
        
        while True:
            chain.append(current)
            index_map[current] = len(chain) - 1
            next_val = sod[current]
            
            # If next_val out of range or sum_of_div=1 => can't form a chain
            if not (1 < next_val <= limit):
                # Mark chain elements visited
                for x in chain:
                    visited_global[x] = True
                break
            
            if next_val in index_map:
                # Found a cycle
                cycle_start_idx = index_map[next_val]
                cycle = chain[cycle_start_idx:]  # The cycle portion
                
                # Check if it is a valid amicable chain (closed loop)
                # We want to ensure the chain loops back to next_val exactly
                # and no element in the cycle is repeated except next_val.
                # By definition of the index_map check, we've found a loop.
                
                # Mark all chain elements visited
                for x in chain:
                    visited_global[x] = True
                
                # The cycle is valid if it loops onto itself (i.e. next_val is the start of the cycle portion).
                # That is already guaranteed by how we sliced the chain.
                
                cycle_length = len(cycle)
                if cycle_length > max_length:
                    max_length = cycle_length
                    best_smallest_member = min(cycle)
                break
            
            # Move on
            current = next_val
            
            # If we've seen `current` globally, no new chain from here
            if visited_global[current]:
                for x in chain:
                    visited_global[x] = True
                break
    
    return best_smallest_member, max_length

def main():
    limit = 1_000_000
    smallest_member, length = find_longest_amicable_chain(limit)
    print(f"The smallest member of the longest amicable chain (<= {limit}) is: {smallest_member}")
    print(f"Length of that chain: {length}")

if __name__ == "__main__":
    main()
