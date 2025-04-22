import nltk
nltk.data.path.append('D:/builds/development/apps/GAI/nltk_data')
nltk.download('stopwords', download_dir='D:/builds/development/apps/GAI/nltk_data')



from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = "This is an example sentence, demonstrating the removal of stop words."

# Tokenize the sentence
tokens = word_tokenize(text)

# Define English stop words
stop_words = set(stopwords.words('english'))

# Filter out stop words
filtered_tokens = [token for token in tokens if token.lower() not in stop_words]

# Print result
print(filtered_tokens)
