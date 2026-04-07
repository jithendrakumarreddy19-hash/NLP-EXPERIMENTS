def plural(word):
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word.endswith(('s', 'x', 'z', 'ch', 'sh')):
        return word + 'es'
    else:
        return word + 's'

# Test
words = ["cat", "baby", "box", "brush"]

for w in words:
    print(w, "→", plural(w))