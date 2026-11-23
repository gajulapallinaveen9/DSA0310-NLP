import re

STOP = {'i', 'a', 'an', 'the', 'is', 'are', 'has', 'have', 'very', 'in', 'of', 'and', 'to'}

def content(sentence):
    return {w for w in re.findall(r'[a-z]+', sentence.lower()) if w not in STOP}

def coherence(text):
    sentences = [s for s in re.split(r'(?<=[.!?])\s+', text.strip()) if s]
    sets = [content(s) for s in sentences]
    sims = [len(a & b) / len(a | b) for a, b in zip(sets, sets[1:])]
    return sum(sims) / len(sims), sims

texts = {
    'Text A': 'I bought a new laptop yesterday. The laptop has a fast processor. '
              'The processor makes the laptop very quick.',
    'Text B': 'I bought a new laptop yesterday. The moon orbits the earth. '
              'Bananas are rich in potassium.',
}
for name, text in texts.items():
    score, sims = coherence(text)
    verdict = 'Coherent' if score >= 0.15 else 'Incoherent'
    print(f'{name}: score={score:.3f} pairs={[round(x, 3) for x in sims]} -> {verdict}')
