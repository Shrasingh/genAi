# Stemming and lemmatization are two methods used in natural language processing (NLP) to reduce words to their base or root form, often called the lemma or stem. Stemming uses rule-based algorithms to strip off suffixes and prefixes, while lemmatization considers the word's context and meaning to find the appropriate base form. 
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download WordNet corpus (only needed once)
nltk.download('wordnet')

# Stemming
stemmer = PorterStemmer()
words = ["run", "runner", "running", "ran", "runs", "eats", "eat", "ate"]
s = [stemmer.stem(word) for word in words]
print("Stemming:", s)

# Lemmatization
lemmatizer = WordNetLemmatizer()
l = [lemmatizer.lemmatize(word) for word in words]
print("Lemmatization:", l)
s