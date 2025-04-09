# Largest Exponential
# Comparing two numbers written in index form like 2^11 and 3^7 is not difficult as any calculator would confirm 2^11 < 3^7
# However, confirming that 632382^518061 > 519432^525806 would be much more difficult, as both numbers contain over three million digits.
# Determine which line number has the greatest numerical value using problem_99_base_exp.txt

import csv
import math

def read_csv_numbers():
    with open("problem_99_base_exp.txt", 'r') as file:
        reader = csv.reader(file)
        return [tuple(map(int, row)) for row in reader]
    
def largest_exponential():
    largest_number = math.log(632383) * 518061
    largest_number_index = 1
    for i in range(len(read_csv_numbers())):
        if math.log(read_csv_numbers()[i][0]) * read_csv_numbers()[i][1] > largest_number:
            largest_number = math.log(read_csv_numbers()[i][0]) * read_csv_numbers()[i][1]
            largest_number_index = i
            print(i, read_csv_numbers()[i])
    return largest_number_index + 1

print(largest_exponential())
