# CAR car -> same case either upper or lower case - Normalization
# Text - part ,segement , chunks ,w ord , sentene

# Normalization
import nltk
from nltk.tokenize import PunktSentenceTokenizer, word_tokenize

# Force nltk to use your custom data path
nltk.data.path.append("D:/builds/development/apps/genAi/nltk_data")

# Download 'punkt' if not already there
nltk.download('punkt', download_dir='D:/builds/development/apps/genAi/nltk_data')

# Use the Punkt tokenizer directly
tokenizer = PunktSentenceTokenizer()

para = "this is a car"
para = para.lower()

print("Word Tokens:", word_tokenize(para))
print("Sentence Tokens:", tokenizer.tokenize(para))


# Segmentation
