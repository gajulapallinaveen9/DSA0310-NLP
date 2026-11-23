import re

MALE = {'john', 'tom'}
FEMALE = {'mary', 'susan'}
OBJECTS = {'book', 'station', 'car', 'laptop'}
PRONOUNS = {'he': 'M', 'him': 'M', 'she': 'F', 'her': 'F', 'it': 'O'}

def mention_type(w):
    if w in MALE:
        return 'M'
    if w in FEMALE:
        return 'F'
    if w in OBJECTS:
        return 'O'
    return None

def resolve(text):
    mentions, links = [], []
    for token in re.findall(r'[A-Za-z]+', text):
        w = token.lower()
        if w in PRONOUNS:
            for name, kind in reversed(mentions):
                if kind == PRONOUNS[w]:
                    links.append((token, name))
                    break
        elif mention_type(w):
            mentions.append((token, mention_type(w)))
    return links

text = 'John met Mary at the station. He gave her a book. It was a gift.'
print('Text:', text)
for pronoun, referent in resolve(text):
    print(pronoun, '->', referent)
