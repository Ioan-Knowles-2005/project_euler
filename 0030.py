#There are only 3 numbers that can be written as the sum of 4th powers of their digits:
#1634 = 1^4 + 6^4 + 3^4 + 4^4, 8208 = 8^4 + 2^4 + 0 + 8^4, 9474 = 9^4 + 4^4 + 7^4 + 4^4
#1 = 1^4 is not included
#The sum of these numbers is 1634 + 8208 + 9474 = 19316
#Find the sum of all the numbers that can be written as the sum of 5th powers of their digits

#A key observation is that for a k-digit number the maximum sum of 5th powers is k * 9^5
#9^5 = 59049
#when k = 2 max = 118098, k=3 max = 177147, k=4 max=236196, k=5 max=295245, k=6 max=354294, k=7 max=413343 
#since the smallest 7 digit number is one million the max sum is below this number so a 7 digit number or above
#can never equal the sum of 5th powers of their digits, so we only search up to 354294
def sum_fifth_powers(n):
    return sum(int(d)**5 for d in str(n))

upper_bound = 354294
def sum_of_results():
    results = []
    for i in range(10, upper_bound + 1): # do from 10 to exclude 1
        if i == sum_fifth_powers(i):
            results.append(i)
    return sum(results)

print(sum_of_results())
