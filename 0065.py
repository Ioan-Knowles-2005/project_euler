# Convergents of e
# e = [2;(1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, 1, ..., 1, 2k, 1, 1, 2k+2, 1, ...)]
# Find the sum of the digits in the numerator of the 100th convergent of the continued fraction e

#pn = an*pn-1 + pn-2
#qn = an*qn-1 + qn-2

#an = 1 if n%3 != 0
#an = 2*n/3 if n%3 == 0

# e ~ 2, 3, 8/3, 11/4, 19/7, 87/32, 106/39

def convergents_of_e():
    list_of_convergents_numerators = [2, 3]
    for n in range(3, 101):
        p_n_minus_one, p_n_minus_two = list_of_convergents_numerators[-1], list_of_convergents_numerators[-2]
        if n % 3 == 0:
            a_n = int(2 * n / 3)
        else:
            a_n = 1
        list_of_convergents_numerators.append(a_n * p_n_minus_one + p_n_minus_two)
    return list_of_convergents_numerators[-1]

def sum_of_digits(n):
    return sum(map(int, str(n)))

print(sum_of_digits(convergents_of_e()))     
        