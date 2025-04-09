#If all the numbers from 1 to 1000 inclusive were written out in words, how many letters would be used
#not including spaces or hyphens
from num2words import num2words

def number_of_letters_for_number_up_to(n):
    list_of_numbers_in_words = []
    number_of_letters = 0
    for i in range(1, n+1):
        list_of_numbers_in_words.append(num2words(i).replace(' ', '').replace('-', ''))
    for num in list_of_numbers_in_words:
        number_of_letters += len(num)
    return number_of_letters


print(number_of_letters_for_number_up_to(1000))