# Counting Fractions
# Consider the fraction, n/d, where n and d are positive integers. If n < d and HCF(n, d) = 1, it is called a reduced proper fraction.
# If we list the set of reduced proper fractions for d <= 8  in ascending order of size,it can be seen that there are 21 elements in this set
# How many elements would be contained in the set of reduced proper fractions for d <= 1,000,000

#This is equivalent to computing Euler’s Totient Function 𝜙(𝑑) for all values of 𝑑 up to 1,000,000

def compute_totient_sieve(limit):
    phi = list(range(limit + 1))  # Initialize phi(n) = n
    
    for i in range(2, limit + 1):
        if phi[i] == i:  # i is a prime
            for j in range(i, limit + 1, i):
                phi[j] *= (i - 1)
                phi[j] //= i  # Apply Euler’s Totient formula
    
    return phi

def counting_fractions():
    phi = compute_totient_sieve(1000000)
    return sum(phi[2:])

print(counting_fractions())