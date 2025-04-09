with open("problem_22_names.txt", "r") as file:
    content = file.read().strip()  # Read the whole file and strip extra whitespace/newlines

# Split the content on commas, then strip spaces and quotes from each name
names_list = [name.strip().strip('"') for name in content.split(",") if name.strip()]
names_list.sort()
#5163 names in file
def alphabetical_score(letter):
    return ord(letter.upper()) - ord('A') + 1

def name_scores():
    name_scores = 0
    for i in range(5163):
        for j in range(len(names_list[i])):
            letter = names_list[i][j]
            name_scores += (i+1) * alphabetical_score(letter)
    return name_scores

print(name_scores())