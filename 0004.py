#The largest palindrome made from the product of two 2-digit numbers is 91*99 = 9009.
#Find the largest palindrome number made from the product of two 3-digit numbers
def largest_palindrome_3_digits():
    largest_palindrome = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):  
            product = i * j
            if str(product) == str(product)[::-1] and product > largest_palindrome: 
                #if product is palindrome and bigger than largest_palindrome, largest palindrome updates
                largest_palindrome = product
    return largest_palindrome

print(largest_palindrome_3_digits())
