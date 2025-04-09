# Square Digit Chains
# A number chain is created by continuously adding the square of the digits in a number to form
#  a new number until it has been seen before.

#For example, 44 -> 32 -> 13 -> 10 -> 1 -> 1
# or:         85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89
# Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. 
# What is most amazing is that EVERY starting number will eventually arrive at 1  or 89.

#How many starting numbers below ten million will arrive at 89?
cache = {1: False, 89: True}

def is_eighty_nine_chain(n):
    if n in cache:
        return cache[n]
    next_n = sum(int(s)**2 for s in str(n))
    result = is_eighty_nine_chain(next_n)
    cache[n] = result
    return result
                
def square_digit_chains():
    total = 0
    for i in range(1, 10000000):
        if is_eighty_nine_chain(i):
            total += 1
    return total

print(square_digit_chains())
