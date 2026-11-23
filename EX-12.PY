grammar = {
    'S':   [['NP', 'VP']],
    'NP':  [['Det', 'N']],
    'VP':  [['V', 'NP']],
    'Det': [['the'], ['a']],
    'N':   [['dog'], ['cat']],
    'V':   [['chased']],
}

def earley(tokens):
    n = len(tokens)
    chart = [[] for _ in range(n + 1)]

    def add(i, state):
        if state not in chart[i]:
            chart[i].append(state)

    add(0, ('GAMMA', ('S',), 0, 0))
    for i in range(n + 1):
        for lhs, rhs, dot, start in chart[i]:
            if dot < len(rhs):
                nxt = rhs[dot]
                if nxt in grammar:                         # PREDICT
                    for prod in grammar[nxt]:
                        add(i, (nxt, tuple(prod), 0, i))
                elif i < n and tokens[i] == nxt:           # SCAN
                    add(i + 1, (lhs, rhs, dot + 1, start))
            else:                                          # COMPLETE
                for l2, r2, d2, s2 in chart[start]:
                    if d2 < len(r2) and r2[d2] == lhs:
                        add(i, (l2, r2, d2 + 1, s2))
    return ('GAMMA', ('S',), 1, 0) in chart[n], chart

tokens = 'the dog chased a cat'.split()
accepted, chart = earley(tokens)
print('Accepted:', accepted)
for lhs, rhs, dot, start in chart[len(tokens)]:
    if dot == len(rhs):
        print(f'{lhs} -> {" ".join(rhs)} .  (start={start})')
print('Accepted:', earley('dog the chased cat'.split())[0])
