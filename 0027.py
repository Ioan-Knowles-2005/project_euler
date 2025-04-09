#Quadratic Primes
#Considering quadratics of the form n^2 + an + b where |a| < 1000 and |b| <= 1000
#Find the product of the coefficients, a and b, for the quadratic expression
# that produces the maximum number of primes for consecutive values of n starting with n = 0

def is_prime(n):
    if n < 2:
        return False
    # Check divisibility up to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_quadratic():
    max_length = 0
    best_a = 0
    best_b = 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            n = 0
            while is_prime(n*n + a*n + b):
                n += 1
            if n > max_length:
                max_length = n
                best_a = a
                best_b = b
    return best_a, best_b, max_length  

print(-61*971)


            
