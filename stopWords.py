from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

ex_text = "The redundant words for analysis will be removed because they are not important. this is not good"
stop_words = set(stopwords.words("english"))
# print(stop_words)
words = word_tokenize(ex_text)
# filtered_sentence = []
# for w in words:
#    if w not in stop_words:
#        filtered_sentence.append(w)
filtered_sentence = [w for w in words if w not in stop_words]
print(filtered_sentence)

