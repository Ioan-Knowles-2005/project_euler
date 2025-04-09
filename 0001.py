#Problem 1 Multiples of 3 and 5
def sum_of_multiples(n):
    sum = 0
    for i in range(n + 1):
        if i % 3 == 0:
            sum += i
        elif i % 5 == 0:
            sum += i
        elif i % 15 == 0:
            sum -= i
        else:
            sum = sum
    return sum

print(sum_of_multiples(1000))