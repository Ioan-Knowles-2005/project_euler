#It can be seen that the number, 125874, and its double 251748
#contain exactly the same digits, but in a different order.
#Find the smallest positive integer x, such that 
# 2x, 3x, 4x, 5x, and 6x, all share the same digits

#To solve this we are going to need to be able to check if numbers have the same digits and i could
#Try do this by sorting numbers and then comparing

def share_digits(a, b, c, d, e, f):
    return sorted(str(a)) == sorted(str(b)) == sorted(str(c)) == sorted(str(d)) == sorted(str(e)) == sorted(str(f))
#returns true if they share the samde digits
def find_smallest_permutated_multiple():
    n=1
    while True:
        if (share_digits(n,2*n, 3*n, 4*n, 5*n, 6*n)):
            return n
        n += 1

print(find_smallest_permutated_multiple())