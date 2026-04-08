import random

text = "I love NLP and I love coding"
words = text.split()

# create pairs
pairs = []
for i in range(len(words)-1):
    pairs.append((words[i], words[i+1]))

# generate text
word = random.choice(words)
print(word, end=" ")

for i in range(5):
    for p in pairs:
        if p[0] == word:
            word = p[1]
            print(word, end=" ")
            break