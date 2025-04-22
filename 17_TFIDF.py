# TF IDF: term frequency inverse document frequency
# TF: frequency of a word within the document
# IDF: frequency of a word across the documents
# how to check which word is more important: 
   # word with the highest TF_IDF score in a document is the most important word in that document
   #if a word consistently has a high TF-IDF score across multiple documents, it could be important across the entire corpus
# the TF_IDF score of a word in a document tells how relevant that word is to the document considering the word's frequency in other documents
   # high TF-IDF indicates the word is relatively unique to the document
   # low TF-IDF: indicates the word is common across many documents in the corpus is less significant

# important -> unique -> TF-IDF -> high
# not important -> not unique -> TF-IDF -> low
# highlight unique words, text classification , info retrieval
# disadvantages: unordered ,semaintic meaning , sparsity
# importnace = TF * IDF



from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
corpus = [
  " i love machine learning",
  
  "i love programming",
  "machine learning is fun"
 ]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)
feature_names = vectorizer.get_feature_names_out()

dense = tfidf_matrix.todense()
denselist = dense.tolist()
df_tfidf = pd.DataFrame(denselist,columns=feature_names)
print(df_tfidf)