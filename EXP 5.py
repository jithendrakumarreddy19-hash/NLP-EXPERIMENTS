from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["running", "played", "studies", "happiness"]

for word in words:
    print(word, "→", ps.stem(word))