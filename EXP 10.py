sentence = [["The", "DT"], ("king", "VBG"), ("is", "VBZ"), ("brave", "JJ")]

rule_find = "VBG"
rule_replace = "NN"
rule_context = "DT"

refined_tags = []
for i in range(len(sentence)):
    word, tag = sentence[i]
    if tag == rule_find and i > 0 and sentence[i-1][1] == rule_context:
        refined_tags.append((word, rule_replace))
    else:
        refined_tags.append((word, tag))

print(refined_tags)