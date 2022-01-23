# Massage the "official" Wordle word list data into a list
with open('wordle.txt') as file:
    data = [word.split('\n')[0] for word in file.readlines()]

# What are the letter frequencies in each of the five letter slots?
# Meaning, what percentage of the first letters are A?  B?  And so forth...
freq = [[0] * 26 for x in range(5)]
for word in data:
    for index, character in enumerate(word):
        freq[index][ord(character) - 97] += 1

# For each word, figure out its relative frequency
d = []
for word in data:
    prob = 1.0
    for index, letter in enumerate(word):
        prob *= freq[index][ord(word[index]) - 97]
    d.append([word, prob])

# Sort the words and their relative frequencies to find the best words
# Only print out the top 20, but you could print them all if you'd like of course
bestWords = sorted(d, key=lambda x: x[1], reverse=True)
for index in range(20):
    print(f"#{index+1:2}: {bestWords[index][0]}")