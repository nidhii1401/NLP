from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


text = "How to remove stop words with NLTK library in Python"
print("Text:", text)


tokens = word_tokenize(text.lower())
print("Tokens:", tokens)


english_stopwords = stopwords.words('english')
tokens_wo_stopwords = [t for t in tokens if t not in english_stopwords]
print("Text without stop words:", " ".join(tokens_wo_stopwords))