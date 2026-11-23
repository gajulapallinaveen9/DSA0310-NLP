import nltk
from nltk import word_tokenize, pos_tag, RegexpParser
from nltk.corpus import wordnet as wn
for pkg in ['punkt', 'punkt_tab', 'averaged_perceptron_tagger',
            'averaged_perceptron_tagger_eng', 'wordnet']:
    nltk.download(pkg, quiet=True)

sentence = 'The quick brown fox jumps over the lazy dog.'
tagged = pos_tag(word_tokenize(sentence))
chunker = RegexpParser('NP: {<DT>?<JJ>*<NN.*>+}')
tree = chunker.parse(tagged)

for sub in tree.subtrees(filter=lambda t: t.label() == 'NP'):
    ws = [w for w, _ in sub.leaves()]
    head = ws[-1]
    syn = wn.synsets(head, pos=wn.NOUN)
    meaning = syn[0].definition() if syn else 'not found'
    print('Noun phrase :', ' '.join(ws))
    print('Head noun   :', head)
    print('Meaning     :', meaning)
    print()
