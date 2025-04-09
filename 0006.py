#Find the difference between the sum of the squares 
#of the first one hundred natural numbers and the square of the sum.
#ie |(1^2 + 2^2 + 3^2 + ...) - (1 + 2 + 3 + ...)^2|
def diff_sum_square(n):
    sum_of_squares = 0
    sum = 0
    for i in range(n+1):
        sum_of_squares += i**2
        sum += i
    square_of_sum = sum ** 2
    difference = sum_of_squares - square_of_sum
    return difference * -1

print(diff_sum_square(100))
