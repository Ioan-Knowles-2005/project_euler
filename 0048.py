#Self powers
#The series 1^1 + 2^2 + 3^3 + ... + 10^10 = 1040571317
#Find the last ten digits of the series 1^1 + 2^2 + ... + 1000^1000

#Can brute force pretty easily

def self_powers():
    total = 0
    for i in range(1, 1001):
        total += i**i
    str_total = str(total)
    return str_total[-10:]

print(self_powers())
