import nltk

patterns = [
    (r'^(the|a|an)$', 'DT'),
    (r'^(and|or|but)$', 'CC'),
    (r'^(over|on|in|at|with)$', 'IN'),
    (r'^(is|are|was|were)$', 'VB'),
    (r'^-?[0-9]+(\.[0-9]+)?$', 'CD'),
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*s$', 'NNS'),
    (r'.*', 'NN'),
]
tagger = nltk.RegexpTagger(patterns)
sentence = 'the dogs were running and jumped over 3 fences'
print(tagger.tag(sentence.split()))
