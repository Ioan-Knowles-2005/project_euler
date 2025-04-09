#Sum of all amicable numbers under 10000
#Amicable numbers are numbers in which the factors of a denoted by d(a)=b and d(b)=a
#Example: a = 220 b = 284
# d(220)= 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284
#d(284)= 1 + 2 + 4 + 71 + 142 = 220
#First we need a way to generate divisors of a number

def sum_of_factors(n):
    sum = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            sum += i
            if n != i:
                sum += n//i
    return sum

def sum_of_amicable_numbers(limit):
    sum_of_divisors = {i: sum_of_factors(i) for i in range(2, limit)}
    amicable_sum = 0
    for i in range(2, limit):
        b = sum_of_divisors[i]
        if b != i and b < limit and sum_of_divisors.get(b, 0) == i:
            amicable_sum += i 
    return amicable_sum

print(sum_of_amicable_numbers(10000))
