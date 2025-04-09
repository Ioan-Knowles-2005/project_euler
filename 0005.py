#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20

def smallest_number_evenly_divisible():
    n = 20
    while True:
        divisible = True
        for i in range(2, 21):
            if n % i != 0:
                divisible = False
                break
        if divisible:
            return n
        n += 20
print(smallest_number_evenly_divisible())

