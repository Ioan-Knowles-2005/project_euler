# Product - Sum Numbers
# A natural number N that can be written as the sum and product of a given set of at least two natural numbers, {a1, a2, ..., ak} is called
# a product sum number: N = a1 + a2 + ... + ak = a1 * a2 * ... * ak
# For example 6 = 1 * 2 * 3 = 1 + 2 + 3
# For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number.
# The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows:
# k = 2: 4 = 2 * 2 = 2 + 2
# k = 3: 6 = 1 * 2 * 3 = 1 + 2 + 3
# k = 4: 8 = 1 * 1 * 2 * 4 = 1 + 1 + 2 + 4
# k = 5: 8 = 1 * 1 * 2 * 2 * 2 = 1 + 1 + 2 + 2 + 2
# k = 6: 12 = 1 * 1 * 1 * 1 * 2 * 6 = 1 + 1 + 1 + 1 + 2 + 6

# Hence for 2 <= k < = 6 the sum of minimal product-sum numbers is 4 + 6 + 8 + 12 = 30, note that 8 is only counted once
# In fact, as the complete set of minimal product-sum numbers for 2 <= k < = 12: {4, 6, 8, 12, 15, 16}, the sum is 61
# What is the sum of all the minimal product-sum numbers for 2 <= k <= 12000

def solve_euler88(limit=12000):
    # We pick a search limit for the product (safe upper bound ~ 2*limit).
    MAX_PRODUCT = 2 * limit

    # best[k] will store the minimal product-sum number for that k
    # Initialize to a large number
    best = [10**20] * (limit + 1)  # index 0..limit

    def dfs(start, length, product, summ):
        """
        Recursively build a factorization (all factors >= 'start'),
        updating minimal product-sums for any valid k encountered.
        :param start:  smallest factor we can use next
        :param length: how many factors chosen so far
        :param product: product of chosen factors so far
        :param summ:    sum of chosen factors so far
        """
        # Compute k for the current set of factors (padded with 1's).
        # k = length + (product - summ)
        k = length + (product - summ)
        if k <= limit:
            # Update best[k] if we found a smaller product-sum
            if product < best[k]:
                best[k] = product

        # Try extending the factorization with a new factor f >= start
        # so that the factor list remains non-decreasing, avoiding duplicates
        f = start
        while True:
            new_product = product * f
            if new_product > MAX_PRODUCT:
                break
            new_sum = summ + f
            if new_product < new_sum:  
                # If product < sum, adding more factors won't fix that,
                # because product grows multiplicatively, sum grows additively.
                # However, it's still possible for large f that product >= sum. So no immediate break.
                pass
            dfs(f, length + 1, new_product, new_sum)
            f += 1

    # Start DFS with no factors chosen, product=1, sum=0
    dfs(start=2, length=0, product=1, summ=0)

    # Collect distinct minimal product-sums for k in [2..limit]
    return sum(set(best[2:limit+1]))

result = solve_euler88(12000)
print("Sum of all minimal product-sum numbers for 2 <= k <= 12000 is:", result)
