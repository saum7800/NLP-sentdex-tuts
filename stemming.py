from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
ex_words = ["pythoner","python","pythoning","pythoned","pythonly"]
for w in ex_words:
    print(ps.stem(w))