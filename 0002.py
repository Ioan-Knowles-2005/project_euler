def even_valued_fibonacci(n):
    a, b = 1, 1
    sum = 0
    while a <= n:
        if a % 2 == 0:
            sum += a
        a,b = b, a+b
    return sum
print(even_valued_fibonacci(4000000))