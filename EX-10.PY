lexicon = {'i': 'PRP', 'we': 'PRP', 'they': 'PRP', 'want': 'VBP', 'can': 'MD',
           'to': 'TO', 'race': 'NN', 'run': 'NN', 'the': 'DT',
           'was': 'VBD', 'long': 'JJ'}

# (from_tag, to_tag, previous_tag)
rules = [('NN', 'VB', 'TO'), ('NN', 'VB', 'MD')]

def tbl_tag(sentence):
    words = sentence.split()
    tags = [lexicon.get(w.lower(), 'NN') for w in words]
    print('Sentence:', sentence)
    print('Initial :', list(zip(words, tags)))
    for frm, to, prev in rules:
        for i in range(1, len(tags)):
            if tags[i] == frm and tags[i - 1] == prev:
                tags[i] = to
                print(f'  rule {frm}->{to} if prev={prev}: changed {words[i]!r}')
    print('Final   :', list(zip(words, tags)))
    print()

for s in ['I want to race', 'they can run', 'the race was long']:
    tbl_tag(s)
