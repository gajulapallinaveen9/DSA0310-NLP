import nltk

grammar = nltk.CFG.fromstring('''
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the' | 'a'
N -> 'dog' | 'cat'
V -> 'chased'
''')

parser = nltk.ChartParser(grammar)
tokens = 'the dog chased a cat'.split()
for tree in parser.parse(tokens):
    print(tree)
    print('Leaves:', tree.leaves())
    print('Height:', tree.height())
