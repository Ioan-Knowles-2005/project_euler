#What is the first triangular number with over five hundred factors
#To generate triangular numbers we simply add the natural numbers
#therefore the formula for the nth triangular number is n(n+1)/2
#We can then iterate through the triangular numbers until we reach one with 
# over 500 factors

def count_factors(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
        i += 1
    return count

def first_triangle_over_divisor_limit(limit):
    n = 1
    while True:
        triangle = n * (n + 1) // 2
        if n % 2 == 0:
            # If n is even, use n/2 and n+1
            fact_count = count_factors(n // 2) * count_factors(n + 1)
        else:
            # If n is odd, use n and (n+1)/2
            fact_count = count_factors(n) * count_factors((n + 1) // 2)
        
        # Check if the number of divisors exceeds the limit
        if fact_count > limit:
            return triangle
        
        n += 1

print(first_triangle_over_divisor_limit(500))

        

