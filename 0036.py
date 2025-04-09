#Double - Base Palindromes
#The decimal number, 585 = 1001001001 in binary is palindromic in both base 2 and base 10
#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2
# Can't include leading zeroes in either base
def is_palindrome(n):
    if str(n) != str(n)[::-1]:
        return False
    return True

def convert_to_binary(num):
    if num == 0:
        return "0"
    
    binary_str = ""
    while num > 0:
        binary_str = str(num % 2) + binary_str
        num //= 2  
    binary_int = int(binary_str)
    return binary_int

def base_2_palindromes():
    sum = 0 
    for i in range(1, 1000000, 2):
        if is_palindrome(i) and is_palindrome(convert_to_binary(i)):
            sum += i
    return sum

print(base_2_palindromes())

 
