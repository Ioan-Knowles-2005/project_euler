# Arranged Probability
# If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were
# taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)*(14/20) = 1/2
# The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random,
# is a box containing eighty-five blue discs and thirty-five red discs.
# By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in total, 
# determine the number of blue discs that the box would contain.

def find_blue_discs(limit=10**12):
    B, T = 85, 120  # Initial known solution

    while T <= limit:
        B, T = 3 * B + 2 * T - 2, 4 * B + 3 * T - 3
        if B % 1001 or T % 1000 == 0:
            print(B, T)
    return B

print(find_blue_discs(limit=10**12))



        
