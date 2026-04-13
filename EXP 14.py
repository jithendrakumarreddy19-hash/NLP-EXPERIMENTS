# Simple agreement: subject + verb

subjects = ["he", "she", "it"]
verbs_singular = ["runs", "eats"]
verbs_plural = ["run", "eat"]

def check_agreement(sentence):
    words = sentence.split()

    if words[0] in subjects and words[1] in verbs_singular:
        return "Correct"
    elif words[0] not in subjects and words[1] in verbs_plural:
        return "Correct"
    else:
        return "Incorrect"

# Test
print(check_agreement("he runs"))
print(check_agreement("they runs"))