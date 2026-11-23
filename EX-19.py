import re

STOP = {'i', 'he', 'she', 'a', 'an', 'the', 'to', 'of', 'my', 'and', 'on', 'in',
        'at', 'is', 'was', 'with', 'out', 'that', 'where', 'people', 'or'}

SENSES = {
    'bank': {
        'bank_finance': 'financial institution where people deposit and borrow money',
        'bank_river': 'sloping land beside a river or lake with water'},
    'bat': {
        'bat_animal': 'small flying mammal that sleeps in a cave at night',
        'bat_sports': 'wooden club used to hit the ball in cricket or baseball'},
}

def words(text):
    return {w for w in re.findall(r'[a-z]+', text.lower()) if w not in STOP}

def lesk(word, sentence):
    context = words(sentence) - {word}
    scores = {sense: len(context & words(gloss))
              for sense, gloss in SENSES[word].items()}
    return max(scores, key=scores.get), scores

tests = [('bank', 'I went to the bank to deposit my money'),
         ('bank', 'The fisherman sat on the bank of the river'),
         ('bat', 'He hit the ball with a bat in the cricket match'),
         ('bat', 'A bat flew out of the cave at night')]
for word, sentence in tests:
    best, scores = lesk(word, sentence)
    print(sentence)
    print('  scores:', scores, '->', best)
