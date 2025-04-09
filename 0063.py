# Powerful Digit Counts
# The 5-digit number 16807 = 7^5, is also a fifth power. Similarly the 9-digit number 134217728 = 8^9 is also a ninth power.
# How many n-digit positive integers exist which are also an nth power?
# Let n = a^b
# len(n) == b only when a < 10
#9^21 has 21 digits but 9^22 also has 21 so we know this is the cut off point

# Can only be an nth power if a^b, a < 10
def nth_roots():
    total = 0
    for a in range(1, 10):
        for b in range(1, 22):
            x = a**b
            if len(str(x)) == b:
                total += 1
                print(f"{a}^{b} = {x}")
    return total

print(nth_roots())

