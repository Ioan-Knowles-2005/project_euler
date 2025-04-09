# Square Root Convergents
# It is possible to show that the square root of two can be expressed as an infinite continued fraction.
# By expanding this for the first three iterations, we get:
# 1 + 1/2 = 3/2 
# 1 + 1/(2 + 1/2) = 7/5 
# 1 + 1/(2 + 1/(2 + 1/2)) = 17/12
# The eighth's expansion = 1393/985 is the first example where the number of digits in the numerator 
# exceeds the number of digits in the denominator.
#In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?

def count_large_numerators(limit):
    p, q = 7, 5  # First expansion
    prev_p, prev_q = 3, 2  # Base values for p and q
    count = 0

    for _ in range(limit):
        if len(str(p)) > len(str(q)):
            count += 1
        # Update sequence
        p, q, prev_p, prev_q = (p + q + prev_p + prev_q), (p+q), p, q
    return count

print(count_large_numerators(1000))
