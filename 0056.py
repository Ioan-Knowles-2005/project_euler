# Powerful Digit Sum
# A googol (10^100) is a massive number: one followed by one-hundred zeros;
# 100^100 is almost unimaginably large: one followed by two-hundred zeros. 
# Despite their size, the sum of the digits in each number is only 1
# Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
# We can brute force this fairly easily

def digit_sum(n):
    n_str = str(n)
    sum_of_digits = 0
    for i in range(len(n_str)):
        sum_of_digits += int(n_str[i])
    return sum_of_digits

def powerful_digit_sum():
    max_sum_of_digits = 0

    for a in range(1, 100):
        for b in range(1, 100):
            if digit_sum(a**b) > max_sum_of_digits:
                max_sum_of_digits = digit_sum(a**b)
    return max_sum_of_digits

print(powerful_digit_sum())


    