import math

docs = {
    'D1': 'the cat sat on the mat',
    'D2': 'the dog sat on the log',
    'D3': 'cats and dogs are pets',
}
tokenized = {d: text.split() for d, text in docs.items()}
N = len(docs)

def idf(term):
    df = sum(1 for toks in tokenized.values() if term in toks)
    return math.log10(N / df) if df else 0.0

def score(query, toks):
    return sum((toks.count(t) / len(toks)) * idf(t) for t in query.split())

query = 'cat sat'
ranking = sorted(((score(query, toks), d) for d, toks in tokenized.items()),
                 reverse=True)
print('Query:', query)
for s, d in ranking:
    print(f'{d}  {s:.4f}  {docs[d]}')
