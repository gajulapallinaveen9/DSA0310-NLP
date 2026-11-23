import random
from collections import defaultdict, Counter

corpus = ('the cat sat on the mat . the dog sat on the rug . '
          'the cat chased the dog . the dog chased the cat .')
tokens = corpus.split()

bigrams = defaultdict(list)
for w1, w2 in zip(tokens, tokens[1:]):
    bigrams[w1].append(w2)

counts = Counter(bigrams['the'])
total = sum(counts.values())
for w, c in sorted(counts.items()):
    print(f'P({w}|the) = {c / total:.3f}')

def generate(start, length=10):
    word, out = start, [start]
    for _ in range(length - 1):
        if word not in bigrams:
            break
        word = random.choice(bigrams[word])
        out.append(word)
    return ' '.join(out)

random.seed(1)
print('Generated:', generate('the', 10))
