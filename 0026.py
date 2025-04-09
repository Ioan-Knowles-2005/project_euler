#Find longest cycle that recurs in 1/d d<1000
#e.g 1/7 = 0.(142857)142857... has a recurring cycle of 6

def recurring_cycle_length(d):
    remainders = {}
    remainder = 1
    pos = 0
    while remainder != 0 and remainder not in remainders:
        remainders[remainder] = pos
        remainder = (remainder * 10) % d
        pos += 1
    if remainder == 0:
        return 0  
    return pos - remainders[remainder]

max_length = 0
result_d = 0

for d in range(2, 1000):
    cycle_len = recurring_cycle_length(d)
    if cycle_len > max_length:
        max_length = cycle_len
        result_d = d

print(result_d, max_length)






