from collections import Counter

data = [("The", "DT"), ("cat", "NN"), ("sat", "VBD"), ("on", "IN"), ("the", "DT"), ("mat", "NN"), ("The", "DT"), ("dog", "NN")]
model = {}
words = set(d[0] for d in data)

for word in words:
    tags = [d[1] for d in data if d[0] == word]
    model[word] = Counter(tags).most_common(1)[0][0]

sentence = ["The", "cat", "dog"]
result = [(word, model.get(word, "NN")) for word in sentence]
print(result)