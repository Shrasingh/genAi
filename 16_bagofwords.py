#  Bag of Words (BoW) is a fundamental text representation technique used in NLP and GenAI. It converts text into numerical vectors based on word frequency, ignoring grammar and word order.

# 🔑 Key Points:
# Text to Numbers: Converts documents into vectors using word counts.

# Vocabulary Creation: Builds a list of all unique words in the corpus.

# Frequency Count: Counts how often each word appears in a document.

# Vector Output: Each document is represented as a vector of word frequencies.

# No Word Order: BoW ignores grammar and sequence of words.

# Applications: Used in text classification, similarity detection, and topic modeling.

# Strength: Simple but effective; forms the base for more advanced NLP models.
# corpus -> documents -> tokenize -> vocab -> frequency -> bag of words
# property - unordered based on frequency , when - text classification data small
# disadvanted - high dimensinality ,sparsity,no semantic meaning 

#BOW
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
corpus = [
    "I love machine learning ",
    "Machine learning is fun"
]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
feature_names = vectorizer.get_feature_names_out()
print(feature_names)
dense = X.todense()
denselist=dense.tolist()
df = pd.DataFrame(denselist,columns=feature_names)
print(df)