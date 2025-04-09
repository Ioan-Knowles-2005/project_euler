#digit cancelling fractions
#An inexperienced mathmetician may think that 49/98 = 4/8 by cancelling the 9s 
#There are exactly four non-trivial examples of this type of fraction,
#less than one in value, and containing two digits in the numerator and denominator.
#If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
from fractions import Fraction

def digit_cancelling_fractions():
    list_of_digit_cancelling_fractions = []
    for i in range(10,100):
        for j in range(i + 1, 100):
            i_str = str(i)
            j_str = str(j)
            common_digits = set(i_str) & set(j_str)
            if common_digits:
                for digit in common_digits:
                    if digit =='0':
                        continue
                    new_i_str = i_str.replace(digit, '', 1)
                    new_j_str = j_str.replace(digit, '', 1)
                    if new_i_str == '' or new_j_str == '':
                        continue
                    new_i = int(new_i_str)
                    new_j = int(new_j_str)
                    if new_j != 0 and i * new_j == j * new_i:
                        list_of_digit_cancelling_fractions.append((i, j))
                        break
    return list_of_digit_cancelling_fractions
valid_fractions = digit_cancelling_fractions()
product = Fraction(1, 1)
for n, d in valid_fractions:
    product *= Fraction(n, d)

print(product)
