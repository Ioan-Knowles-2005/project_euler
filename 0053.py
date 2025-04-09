#Find how many values of n choose r are greater than a million when 1<= n <= 100 where r <= n
#formula for n choose r is n!/(r!*(n-r)!)
#the first value greater than a million is 23C10
#23 has 4 values over a million 23C10, 23C11, 23C12, 23C13

import math

def nCr(n, r):
    return math.comb(n, r)

def values_greater_than_k(n, k):
    number_of_values_greater_than_k = 0
    for i in range(23, n+1):
        for j in range(4, i):
            if nCr(i, j) >= k:
                number_of_values_greater_than_k += 1
    return number_of_values_greater_than_k

print(values_greater_than_k(100, 1000000))


