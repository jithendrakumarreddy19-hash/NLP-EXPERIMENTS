grammar = {
    "S": [("NP VP", 1.0)],
    "NP": [("she", 0.5), ("he", 0.5)],
    "VP": [("runs", 0.6), ("eats", 0.4)]
}

def pcfg_parse(sentence):
    words = sentence.split()
    prob = 1.0

    for word in words:
        found = False
        for rules in grammar.values():
            for rhs, p in rules:
                if word in rhs:
                    prob *= p
                    found = True
        if not found:
            return 0

    return prob

# Test
print("Probability:", pcfg_parse("she runs"))