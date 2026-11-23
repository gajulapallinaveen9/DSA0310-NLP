from nltk.stem import PorterStemmer

ps = PorterStemmer()
words = ['caresses', 'ponies', 'running', 'happily',
         'generalization', 'relational', 'studies', 'flies']
for w in words:
    print(w.ljust(16), '->', ps.stem(w))
