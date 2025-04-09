#What is the index of the first fibonacci number to have over 1000 digits

def fibonacci(digit_limit):
    a, b = 1, 1
    idx = 1
    while len(str(a)) < digit_limit:
        a, b = b, a+b
        idx += 1
    return idx

print(fibonacci(1000))
