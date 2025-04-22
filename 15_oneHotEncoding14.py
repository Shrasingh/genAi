# one hot encoding -binary based encoding i love machinelearing -> 100 010 001
#  
import numpy as np

def one_hot_encode(word,vocab):
    vector = np.zeros(len(vocab))
    vector[vocab.index(word)]=1
    return vector
vocab = ["I","LOVE" ,"MACHINE","LEARNING"]
one_hot = one_hot_encode("I",vocab)
print(one_hot)
one_hot = one_hot_encode("LOVE",vocab)
print(one_hot)
one_hot = one_hot_encode("MACHINE",vocab)
print(one_hot)
one_hot = one_hot_encode("LEARNING",vocab)
print(one_hot)
#text to numericak - basic method
# simple to use 
# mapping of words to numbers
# disadvantes - high dimensinality,sparsity,no semantic meaning , out of vocabulary, can not add later



import pandas as pd
data = { 'color': ['red','blue','black','green']}
df = pd.DataFrame(data)
print(df)
one_hot_encoded = pd.get_dummies(df,columns=['color'])
print(one_hot_encoded)



from sklearn.preprocessing import OneHotEncoder

# Define vocabulary as a list
vocabulary = ["apple", "banana", "lemon", "mango"]

# Convert list to 2D array (required format for sklearn)
vocab_array = np.array(vocabulary).reshape(-1, 1)  # shape: (4, 1)

# Initialize the OneHotEncoder with sparse_output=False to get dense array
one_hot_encoder = OneHotEncoder(sparse_output=False)

# Fit and transform the vocabulary
one_hot_encoded = one_hot_encoder.fit_transform(vocab_array)

# Display each word with its one-hot encoded vector
print("One-Hot Encoding using scikit-learn:")
for word, vec in zip(vocabulary, one_hot_encoded):
    print(f"{word}: {vec}")