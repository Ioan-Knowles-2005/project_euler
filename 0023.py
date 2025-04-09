#Non-Abundant Sums
#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
#Abundant numbers are numbers which the sum of their divisors are greater than the number itself
#The smallest abundant number is 12, so the smallest number which can be written as a sum of two abundant
#numbers is 24
#Any number above 28123 can be written as the sum of two abundant numbers
#To solve this we will write a function which generates all abundant numbers up to 28123
#Then iterate along this list and form a list of numbers which can't be written as the sum of two abundant numbers

def sum_of_divisors(n):
    total = 1
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total

abundants = [i for i in range(12, 28124) if sum_of_divisors(i) > i]

abundant_sums = set()
for i in abundants:
    for j in abundants:
        s = i + j
        if s <= 28123:
            abundant_sums.add(s)
        else:
            break

result = sum(i for i in range(1, 28124) if i not in abundant_sums)
print(result)