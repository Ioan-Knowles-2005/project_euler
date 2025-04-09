# Lychrel Numbers
# If we take 47 and add the reverse, 74: 47 + 74 = 121, which is palindromic
# Not all numbers produce palindromes so quickly. For example 
# 349 + 943 = 1292
# 1292 + 2921 = 4213
# 4213 + 3124 = 7337
# 349 took three iterations to become palindromic
# Although no one has proved it yet, it is thought that some numbers, like 196,
# never produce a palindrome. A number that never forms a palindrome through the reverse and add process 
# is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem,
#  we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below 
# ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, 
# with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 
# is the first number to be shown to require over fifty iterations before producing a palindrome
# Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994
# How many Lychrel numbers are there below ten-thousand?
def is_palindrome(n):
    if str(n) != str(n)[::-1]:
        return False
    return True

def is_lychrel(n):
    str_n = str(int(str(n)) + int(str(n)[::-1]))
    iterations = 0
    while iterations <= 50:
        if str_n == str_n[::-1]:
            return False
        else:
            str_n = str(int(str_n) + int(str_n[::-1]))
        iterations += 1
    return True

def lychrel_numbers(limit):
    number_of_lychrels = 0
    for i in range(limit+1):
        if is_lychrel(i):
            number_of_lychrels += 1
    return number_of_lychrels

print(lychrel_numbers(10000))
