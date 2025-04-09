#Starting with the number 1 and moving to the right in a clockwise direction a 5x5 spiral is formed as follows:
#   21 22 23 24 25
#   20  7  8  9 10
#   19  6  1  2 11
#   18  5  4  3 12
#   17 16 15 14 13
#
#It can be verified that the sum of the numbers on the diagonals is 101
#What is the sum of the numbers on the diagonals in a 1001x1001 spiral formed in the same way?

def spiral_diagonals(n):
    sum = 1 #This is the centre
    layers = (n-1)//2 # There are (n-1)/2 layers surrounding the centre
    for i in range(1, layers + 1):
        # For layer k, the side length is (2k + 1).
        # The four corners of that layer are:
        #   (2k+1)^2, (2k+1)^2 - 2k, (2k+1)^2 - 4k, (2k+1)^2 - 6k.
        # Their sum is:
        sum += 4 * (2 * i + 1) ** 2 - 12 * i
    return sum
print(spiral_diagonals(1001))