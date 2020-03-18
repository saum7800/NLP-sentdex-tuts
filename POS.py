import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

ex_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(ex_text)