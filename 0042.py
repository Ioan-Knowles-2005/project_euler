#Coded triangle problem
#By converting each letter in a word to a number corresponding to its alphabetical
# position and adding these values we form a word value.
#If the word value is a triangle number then we shall call the word a triangle word.
#Using problem_42_words.txt how many are triangle words

with open("problem_42_words.txt", "r") as file:
    content = file.read().strip()  # Read the whole file and strip extra whitespace/newlines

# Split the content on commas, then strip spaces and quotes from each name
words_list = [word.strip().strip('"') for word in content.split(",") if word.strip()]
words_list.sort()
#1786 words in list

def is_triangle_number(n):
    for i in range(1, n):
        if n == 1/2*(i)*(i+1):
            return True
    return False

def alphabetical_score(letter):
    return ord(letter.upper()) - ord('A') + 1

def word_score(word):
    return sum(alphabetical_score(ch) for ch in word)

scores = [word_score(w) for w in words_list]

max_score = max(scores)  # The largest word score
# Generate triangle numbers T_i = i*(i+1)//2 up to >= max_score
triangle_nums = set()
i = 1
while True:
    t = i * (i + 1) // 2
    if t > max_score:
        break
    triangle_nums.add(t)
    i += 1

triangle_word_count = sum(1 for s in scores if s in triangle_nums)
print(triangle_word_count)




