import nltk
from nltk.corpus import wordnet as wn
nltk.download('wordnet', quiet=True)

for s in wn.synsets('bank')[:3]:
    print(s.name(), '-', s.definition())

dog = wn.synset('dog.n.01')
print('Lemmas    :', dog.lemma_names())
print('Hypernyms :', [h.name() for h in dog.hypernyms()])

good = wn.synset('good.a.01')
print('Antonym   :', good.lemmas()[0].antonyms()[0].name())
print('Similarity(dog, cat):', dog.path_similarity(wn.synset('cat.n.01')))
