# Totient Sum
#Euler's totient function phi(n) sometimes called the phi function is defined as the number of positive integers not exceeding n which are relatively
# prime to n. For example as 1, 2, 4, 5, 7 and 8 are all less than or equal to nine and relatively prime to nine, phi(9) = 6
# It can be seen that n = 6, produces a maximum n / phi(n) for n <= 10 as 6 / phi(6) = 3
# Find the value of n <= 1,000,000 for which n / phi(n) is a maximum
import math

def totient_function(n):
    count = 0
    for i in range(1, n):
        if math.gcd(i, n) == 1:
            count += 1
    return count

def totient_sum():
    max_totient_sum = (0, 0)
    for n in range(2, 1000001, 2):
        totient_sum = n / totient_function(n)
        if totient_sum > max_totient_sum[1]:
            max_totient_sum = (n, totient_sum)    
            print(max_totient_sum)
    return max_totient_sum

print(totient_sum())