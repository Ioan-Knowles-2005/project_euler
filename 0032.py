#An n-digit number is pandigital if it makes use of all digits 1 to n exactly once
#For example, the 5-digit number 15234 is 1 through 5 pandigital
#The product 7254 is unusual, as the identity 39 * 186 = 7254, containing multiplicand, multiplier and product is
# 1 through 9 pandigital

#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#
def is_pandigital(a, b, c):
    """Return True if the concatenation of a, b, and c is 1 through 9 pandigital."""
    s = str(a) + str(b) + str(c)
    return len(s) == 9 and set(s) == set("123456789")


def sum_of_products():
    products = set()
    #for one digit multiplier and four digit multiplicand
    for a in range(1, 10):
        for b in range(1000, 10000):
            c = a * b
            if is_pandigital(a, b, c):
                products.add(c)
    #for two digit and three digit
    for a in range(10,100):
        for b in range(100, 1000):
            c = a * b
            if is_pandigital(a, b, c):
                products. add(c)
    return sum(products)
print(sum_of_products())
