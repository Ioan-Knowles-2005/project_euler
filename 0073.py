# Consider the fraction n/d where n and d are positive integers. If n < d and HCF(n,d)=1, it is called a proper 
# reduced fraction. If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we get:
# 1/8, 1/7, 1/6, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 2/3, 5/7, 3/4, 4/5, 5/6, 6//7, 7/8
#It can be seen that there are 3 fractions between 1/3 and 1/2
# How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d<= 12000

from math import gcd

def count_fractions_between(lower_bound, upper_bound, max_d):
    count = 0 
    for d in range(1, max_d + 1):
        for n in range(1, d):
            if gcd(n, d) == 1:
                fraction_value = n / d
                if lower_bound < fraction_value < upper_bound:
                    count += 1
                    if count % 100 == 0:
                        print(count)
    return count
#This is O(n^2) time



# Given problem constraints
max_denominator = 12000
result = count_fractions_between(1/ 3, 1/ 2, max_denominator)
print("Number of fractions between 1/3 and 1/2 for d ≤ 12000:", result)