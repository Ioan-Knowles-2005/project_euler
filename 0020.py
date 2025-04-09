#Find the sum of the digits of n!, in this question 100!
import math

def fct(n):
    return math.factorial(n)

def sum_of_fct(n):
    m = fct(n)
    num_str = str(m)
    list_of_digits =[]
    sum_of_digits = 0
    for i in range(len(num_str)):
        list_of_digits.append(int(num_str[i]))
    for digit in list_of_digits:
        sum_of_digits += digit
    return sum_of_digits

print(sum_of_fct(100))
