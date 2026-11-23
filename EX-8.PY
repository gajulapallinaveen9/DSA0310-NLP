from collections import defaultdict, Counter

train = [
    [('the', 'DT'), ('dog', 'NN'), ('barks', 'VBZ')],
    [('a', 'DT'), ('cat', 'NN'), ('sleeps', 'VBZ')],
    [('the', 'DT'), ('cat', 'NN'), ('chases', 'VBZ'), ('a', 'DT'), ('dog', 'NN')],
    [('i', 'PRP'), ('run', 'VB')],
    [('we', 'PRP'), ('run', 'VB')],
    [('a', 'DT'), ('run', 'NN')],
]

counts = defaultdict(Counter)
for sent in train:
    for word, tag in sent:
        counts[word][tag] += 1

def tag_sentence(sentence):
    result = []
    for w in sentence.lower().split():
        if w in counts:
            tag, c = counts[w].most_common(1)[0]
            p = c / sum(counts[w].values())
        else:
            tag, p = 'NN', 0.0
        result.append(f'{w}/{tag}({p:.2f})')
    return ' '.join(result)

for s in ['the dog chases a cat', 'we run', 'the bird sleeps']:
    print(s, '->', tag_sentence(s))
