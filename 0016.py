#2^15 = 32768 and its digits is 3+2+7+6+8=26
#What is the sum of the digits of the number 2^1000
def sum_of_digits(n):
    num_str = str(n)
    list_of_digits =[]
    sum = 0
    for i in range(len(num_str)):
        list_of_digits.append(int(num_str[i]))
    for j in range(len(list_of_digits)):
        sum += list_of_digits[j]
    return sum
print(sum_of_digits(2**1000))
