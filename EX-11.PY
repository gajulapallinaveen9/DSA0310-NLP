grammar = {
    'S':   [['NP', 'VP']],
    'NP':  [['Det', 'N']],
    'VP':  [['V', 'NP'], ['V']],
    'Det': [['the'], ['a']],
    'N':   [['dog'], ['cat'], ['ball']],
    'V':   [['chased'], ['saw']],
}

def parse(symbol, tokens, pos):
    if symbol not in grammar:                      # terminal
        if pos < len(tokens) and tokens[pos] == symbol:
            yield pos + 1
        return
    for production in grammar[symbol]:
        yield from expand(production, tokens, pos)

def expand(symbols, tokens, pos):
    if not symbols:
        yield pos
        return
    for p in parse(symbols[0], tokens, pos):
        yield from expand(symbols[1:], tokens, p)

def recognize(sentence):
    tokens = sentence.split()
    return any(end == len(tokens) for end in parse('S', tokens, 0))

for s in ['the dog chased a cat', 'a cat saw the ball',
          'the dog chased', 'dog the chased cat', 'the dog']:
    print(f'{s!r:24} ->', 'Accepted' if recognize(s) else 'Rejected')
