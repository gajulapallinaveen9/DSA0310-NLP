import spacy

nlp = spacy.load('en_core_web_sm')
text = 'Apple Inc. was founded by Steve Jobs in Cupertino, California in 1976.'
doc = nlp(text)

for ent in doc.ents:
    print(ent.text.ljust(14), ent.label_.ljust(8), spacy.explain(ent.label_))
