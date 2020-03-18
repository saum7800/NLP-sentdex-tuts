from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "this is just to check how's the weather today tokenizer. Splitting into multiple sentences here"
print(word_tokenize(example_text))
print(sent_tokenize(example_text))
