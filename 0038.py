#Pandigital multiples
#Take 192 and multiply by 1, 2, 3: [192, 384, 576]
#By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated
#product of 192 and (1, 2, 3)
#The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, 5, giving the pandigital, 918273645
#which is the concatenated product of 9 and (1, 2, 3, 4, 5)
#What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an 
# integer with (1, 2, ..., n) where n > 1

def is_pandigital(s):
    return len(s) == 9 and set(s) == set("123456789")

max_pandigital = 0

# The base number must be less than 10000, otherwise the concatenated product would exceed 9 digits quickly.
for i in range(1, 10000):
    concatenated_product = ""
    n = 1
    while len(concatenated_product) < 9:
        concatenated_product += str(i * n)
        n += 1
    if len(concatenated_product) == 9 and is_pandigital(concatenated_product):
        pandigital_num = int(concatenated_product)
        if pandigital_num > max_pandigital:
            max_pandigital = pandigital_num

print("The largest 1 to 9 pandigital concatenated product is:", max_pandigital)
