import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

text = "Natural language processing is amazing"
tokens = nltk.word_tokenize(text)
tags = nltk.pos_tag(tokens)
print(tags)