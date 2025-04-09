#A pythagorean triplet is 3 numbers a,b,c st a^2 +b^2 = c^2
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product a*b*c
#We could try generate pythagorean triplets and then check to see if their sum equals 1000
import numpy as np
def pythagorean_triple_product(): 
    for a in range(1, 334):
        for b in range(a, 500):
            c_val = np.sqrt(a**2 + b**2)
            if c_val.is_integer():
                c = int(c_val)
                if b < c and (a + b + c) == 1000:
                    return a, b, c
    return None
    
print(pythagorean_triple_product())
        