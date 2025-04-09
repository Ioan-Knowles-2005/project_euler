#What is the millionth lexicographic permutation of 0,1,2,3,4,5,6,7,8,9

#This means the permutations in numerical order 
#The first permutation is 0123456789
#The second permutation is 0123456798

import math 

def nth_permutation(seq, n):
    seq = list(seq)
    permutation = []
    n -= 1
    while seq:
        f = math.factorial(len(seq) - 1)
        index = n // f
        permutation.append(seq.pop(index))
        n %= f
    return ''.join(map(str, permutation))

print(nth_permutation('0123456789', 1000000))