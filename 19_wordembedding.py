# text to numerical
# one hot encoding - binary based encoding  - i love ml -> 10000
import numpy as np 

def one_hot_encode(word,vocab):
    vector = np.zeroes(len(vocab))
    vector[vocab.index(word)]=1
    return vector

vocab = ["I","LOVE" ,"MACHINE","LEARNING"]
one_hot = one_hot_encode("love",vocab)
print(one_hot)
# small simple 
# high dimensinality,sparsity,no semantic meaning , out of vocabulary
