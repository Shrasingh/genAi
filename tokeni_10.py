# after cleaing we should do tokenization ,easy management - vector , can tell parts of speech
# context gone , multiple meaning of same word

import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt', download_dir='D:/builds/development/apps/genAi/nltk_data')
nltk.download('punkt', download_dir='D:/builds/development/apps/genAi/nltk_data')

sentence = "The quick brown fox jumps over the lazy dog."
tokens= word_tokenize(sentence)
print(tokens)