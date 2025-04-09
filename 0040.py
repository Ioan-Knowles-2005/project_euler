#Champernowne's Constant
#An irrational decimal fraction is created by concatenating the positive integers:
# 1234567891011121314151617181920212223242526272829303132333435...
#It can be seen that the twelth digit of the fractional part is 1
#If dn represents the nth digit of the fractional part find the valued of the following expression:
#d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000
#ie the 1st, 10th, 100th, 1000th, 10000th, 100000th, 1000000th digit

def irrational_product():
    irrational_string = ''
    for i in range(1, 1000001):
        irrational_string += str(i)
    product = int(irrational_string[0]) * int(irrational_string[9]) * int(irrational_string[99]) * int(irrational_string[999]) * int(irrational_string[9999]) * int(irrational_string[99999]) * int(irrational_string[999999])
    return product

print(irrational_product())