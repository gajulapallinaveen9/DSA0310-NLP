import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download('wordnet', quiet=True)

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
words = ['running', 'flies', 'better', 'studies', 'cars']

print('Word'.ljust(10) + 'Stem'.ljust(10) + 'Lemma(n)'.ljust(12) + 'Lemma(v)')
for w in words:
    print(w.ljust(10) + stemmer.stem(w).ljust(10)
          + lemmatizer.lemmatize(w, 'n').ljust(12) + lemmatizer.lemmatize(w, 'v'))
