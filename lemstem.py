# stemming and lemmatization
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
