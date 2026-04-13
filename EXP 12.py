def earley_parser(grammar, sentence):
    n = len(sentence)
    chart = [set() for _ in range(n+1)]

    # Add start rule
    chart[0].add(("S'", ("S",), 0))

    for i in range(n+1):
        changed = True
        while changed:
            changed = False
            for state in list(chart[i]):
                lhs, rhs, dot = state

                # If not complete
                if dot < len(rhs):
                    symbol = rhs[dot]

                    # Predictor
                    if symbol in grammar:
                        for rule in grammar[symbol]:
                            new_state = (symbol, tuple(rule), 0)
                            if new_state not in chart[i]:
                                chart[i].add(new_state)
                                changed = True

                    # Scanner
                    elif i < n and symbol == sentence[i]:
                        chart[i+1].add((lhs, rhs, dot+1))

                # Completer
                else:
                    for prev in chart[i]:
                        plhs, prhs, pdot = prev
                        if pdot < len(prhs) and prhs[pdot] == lhs:
                            new_state = (plhs, prhs, pdot+1)
                            if new_state not in chart[i]:
                                chart[i].add(new_state)
                                changed = True

    return any(state == ("S'", ("S",), 1) for state in chart[n])


# Grammar
grammar = {
    "S": [["a", "S", "b"], ["a", "b"]]
}

print(earley_parser(grammar, "aabb"))