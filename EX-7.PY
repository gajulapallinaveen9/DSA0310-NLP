import nltk
from nltk import word_tokenize, pos_tag
for pkg in ['punkt', 'punkt_tab', 'averaged_perceptron_tagger',
            'averaged_perceptron_tagger_eng']:
    nltk.download(pkg, quiet=True)

text = 'The quick brown fox jumps over the lazy dog.'
print(pos_tag(word_tokenize(text)))
