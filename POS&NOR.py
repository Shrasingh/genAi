
# pos - categorize each word in a sentence into its grammitical function(nouns, verbs, adjectives etc)
# after tokenizatip to understand the grammitical structure of the text
# enhances understanding pf the text's meaning ans structure
# useful for parsing and ner
# disadvantages - requires accurate model,which can be language dependent,may struggle with ambbiguous words based on context
import nltk 
from nltk.tokenize import word_tokenize
nltk.download('puntk')
nltk.download('averaged_percception_tagger')

sentence = "The quick brown fox jumps over the lazy dog."
tokens= word_tokenize(sentence)
tag = nltk.pos_tag(tokens)
print(tag)

# 