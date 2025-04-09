#Longest collatz chain 


def max_chain():
    max_chain_number = 0
    max_count = 0

    for original in range(3, 1000001):
        n = original  
        count = 1     
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            count += 1
        if count > max_count:
            max_count = count
            max_chain_number = original  
    
    return max_chain_number

# Example usage:
print(max_chain())


