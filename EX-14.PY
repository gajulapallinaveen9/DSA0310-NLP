import nltk

grammar = nltk.CFG.fromstring('''
S -> NPsg VPsg | NPpl VPpl
NPsg -> Det Nsg
NPpl -> Det Npl
VPsg -> Vsg | Vsg NPsg | Vsg NPpl
VPpl -> Vpl | Vpl NPsg | Vpl NPpl
Det -> 'the'
Nsg -> 'dog' | 'cat'
Npl -> 'dogs' | 'cats'
Vsg -> 'barks' | 'chases'
Vpl -> 'bark' | 'chase'
''')
parser = nltk.ChartParser(grammar)

def check(sentence):
    return len(list(parser.parse(sentence.split()))) > 0

for s in ['the dog barks', 'the dogs bark', 'the dogs barks',
          'the dog bark', 'the cat chases the dogs', 'the cats chases the dog']:
    print(s, '->', 'Agreement OK' if check(s) else 'Agreement ERROR')
