# Counting Summations
# It is possible to write five as a sum in exactly six different ways:
# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1
# How many different ways can one hundred be written as a sum of at least two positive integers?

# p(n) = p(n-1) + p(n-2) + p(n-3) + ... + p(1)
#p()

def count_partitions(n):
    partitions = [0] * (n + 1)
    partitions[0] = 1  # Base case
    if n == 0:
        return 0
    for num in range(1, n):  # Iterate through numbers 1 to n-1
        for i in range(num, n + 1):
            partitions[i] += partitions[i - num]

    return partitions[n] 

print(count_partitions(100))