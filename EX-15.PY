from nltk import PCFG, ViterbiParser

grammar = PCFG.fromstring('''
S -> NP VP [1.0]
NP -> Det N [0.5] | NP PP [0.125] | 'John' [0.375]
VP -> V NP [0.75] | VP PP [0.25]
PP -> P NP [1.0]
Det -> 'the' [1.0]
N -> 'dog' [0.5] | 'park' [0.5]
V -> 'saw' [1.0]
P -> 'in' [1.0]
''')

parser = ViterbiParser(grammar)
tokens = 'John saw the dog in the park'.split()
for tree in parser.parse(tokens):
    print(tree)
