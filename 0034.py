#145 is a curious number as 1! + 4! + 5! = 145
#Find the sum of all numbers which are equal to the sum of the factorial of their digits
#Note:1! = 1 and 2! = 2 are not sums so they aren't included
#for a k-digit number the max sum is k*9! = k*362880
#(k=8 max=2903040 the smallest 8-digit number is 10000000 so can't work)
# therefore can stop at k=7 where the max sum = 2540160



import math
def sum_factorial(n):
    return sum(int(math.factorial(int(d))) for d in str(n))
    
upper_bound = 2540160
def sum_factorial_digit_numbers():
    results = []
    for i in range(10, upper_bound + 1): #from 10 to exclude 1 and 2
        if i == sum_factorial(i):
            results.append(i)
    return sum(results)

print(sum_factorial_digit_numbers())